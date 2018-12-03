class Person(object):

    def __init__(self, ime, priimek, starost):
        self.ime = ime
        self.priimek = priimek
        self.starost = starost

    def show_person(self):
        print "Ime: {}\nPriimek: {}\nStarost: {}".format(self.ime,
                                                         self.priimek,
                                                         self.starost)
    def age_in_months(self):
         return self.starost*12

if __name__ == '__main__':
    oseba = Person("Janez", "Kranjski", 33)
    oseba.show_person()
    print oseba.age_in_months()
    print type(oseba)

    person_list = [Person("ime1", "fo", 99), Person("ime2", "kfi", 32), Person("ime3", "kfoe", 87)]
    for o in person_list:
        o.show_person()
        print o.ime