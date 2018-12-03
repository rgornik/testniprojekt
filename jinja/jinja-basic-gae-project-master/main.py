#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Sporocilo, Film
from google.appengine.api import users
from google.appengine.api import urlfetch
import json

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("home.html")

class OmeniHandler(BaseHandler):
    def get(self):
        name = "Jaka"
        rezultat = Sporocilo.query().fetch()
        params = {"name": name,
                  "sporocila": rezultat}

        return self.render_template("omeni.html", params=params)

class RezultatHandler(BaseHandler):
    def post(self):
        vnos = self.request.get("vnos")
        sp = Sporocilo(vnos=vnos)
        sp.put()
        return self.write("Vnesel si: {}".format(vnos))

class BMIHandler(BaseHandler):
    def get(self):
        return self.render_template("bmicalc.html")
    def post(self):
        visina = float(self.request.get("visina"))
        teza = float(self.request.get("teza"))
        bmi = teza / visina**2
        return self.write("BMI: {}".format(bmi))

class UrediSporociloHandler(BaseHandler):
    def get(self, sporocilo_id):
        sporocilo = Sporocilo.get_by_id(int(sporocilo_id))
        params = {"sporocilo": sporocilo}
        return self.render_template("uredi_sporocilo.html", params=params)

    def post(self, sporocilo_id):
        vnos = self.request.get("vnos")
        sporocilo = Sporocilo.get_by_id(int(sporocilo_id))
        sporocilo.vnos = vnos
        sporocilo.put()
        return self.redirect_to("omeni")

class IzbrisiSporociloHandler(BaseHandler):
    def get(self, sporocilo_id):
        sporocilo = Sporocilo.get_by_id(int(sporocilo_id))
        params = {"sporocilo": sporocilo}
        return self.render_template("izbrisi_sporocilo.html", params=params)

    def post(self, sporocilo_id):
        sporocilo = Sporocilo.get_by_id(int(sporocilo_id))
        sporocilo.key.delete()
        return self.redirect_to("omeni")

class FilmHandler(BaseHandler):
    def get(self):
        all_films = Film.query().fetch()
        params = {"all_films": all_films}
        return self.render_template("vnos_filma.html", params=params)
    def post(self):
        naslov = self.request.get("naslov")
        reziser = self.request.get("reziser")
        igralec = self.request.get("igralec")
        zanr = self.request.get("zanr")
        leto_prod = int(self.request.get("leto_prod"))
        #dropdown!
        ocena = int(self.request.get("ocena"))
        slika = self.request.get("slika")
        ogledano = bool(int(self.request.get("ogledano")))
        komentar = self.request.get("komentar")

        film = Film(naslov=naslov,
                  reziser=reziser,
                  glavni_igralec=igralec,
                  zanr=zanr,
                  leto_produkcije=leto_prod,
                  ocena=ocena,
                  slika=slika,
                  ogledano=ogledano,
                  komentar=komentar)

        film.put()
        return self.redirect_to("filmi")

class LoginHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            logiran = True
            logout_url = users.create_logout_url("/")

            params = {"logiran": logiran,
                      "logout_url": logout_url,
                      "user": user}
        else:
            logiran = False
            login_url = users.create_login_url("/logiranje")

            params = {"logiran": logiran,
                      "login_url": login_url}

        return self.render_template("samo_za_logiranje.html", params=params)

class PeopleHandler(BaseHandler):
    def get(self):
        with open("people.json", "r") as json_file:
            data = json_file.read()
        jdata = json.loads(data)
        weather_url = "http://api.openweathermap.org/data/2.5/weather?apikey=4e5cbbfb46a984054d59b5ca7f978335&q=Ljubljana&units=metric"
        weather_data = urlfetch.fetch(weather_url)
        weather_data = json.loads(weather_data.content)
        params = {"people": jdata,
                  "weather": weather_data}
        return self.render_template("people.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/omeni', OmeniHandler, name="omeni"),
    webapp2.Route('/rezultat', RezultatHandler),
    webapp2.Route('/bmi', BMIHandler),
    webapp2.Route('/sporocilo/<sporocilo_id:\d+>/uredi', UrediSporociloHandler),
    webapp2.Route('/sporocilo/<sporocilo_id:\d+>/izbrisi', IzbrisiSporociloHandler),
    webapp2.Route('/dodaj_film', FilmHandler, name="filmi"), #name za redirect to
    webapp2.Route('/logiranje', LoginHandler),
    webapp2.Route('/people', PeopleHandler),
], debug=True)
