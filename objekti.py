class MojPrviClass(object):

    def __init__(self, ime):
        self.ime = ime
        print "Pozdrav iz __init__ - {}".format(ime)
        self.pozdravi()

    def pozdravi(self):
        print "Pozdravljen {}".format(self.ime)

mojclass = MojPrviClass("Jaz")
mojclass.pozdravi()
print mojclass.ime