class Stavba(object):

    def __init__(self, st_vrat, st_oken):
        self.st_vrat = st_vrat
        self.st_oken = st_oken

    def show(self):
        print "Stavba\nst. vrat: {}\nst. oken: {}".format(self.st_vrat, self.st_oken)

class Blok(Stavba):

    def __init__(self,st_vrat, st_oken, st_dvigal):
        super(Blok, self).__init__(st_vrat, st_oken)
        self.st_dvigal = st_dvigal

    def show(self):
        print "Blok\nst. vrat: {}\nst. oken: {}\nst. dvigal: {}".format(self.st_vrat,
                                                                        self.st_oken,
                                                                        self.st_dvigal)


if __name__ == '__main__':
    stavba = Stavba(1, 2)
    stavba.show()

    blok = Blok(80, 160, 2)
    blok.show()
