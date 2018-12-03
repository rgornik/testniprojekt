class Oseba(object):

    def __init__(self, ime):
        self.ime = ime

class ContactBook(object):

    def __init__(self):
        self.entries = []

    def add_contact(self, ime):
        self.entries.append(Oseba(ime))

    def update_contract(self, old_ime, new_ime):
        for person in self.entries:
            if person.ime == old_ime:
                person.ime = new_ime

    def delete_contract(self, ime):
        for n, person in enumerate(self.entries):
            if person.ime == ime:
                index_to_delete = n
        self.entries.pop(index_to_delete)

    def __str__(self):
        my_str = ""
        for person in self.entries:
            my_str += person.ime + "\n"

        return my_str

if __name__ == '__main__':
    contact_book  = ContactBook()
    contact_book.add_contact("Janez")
    print contact_book #klice se __str__ metoda objekta
    contact_book.update_contract("Janez", "Josko")
    print contact_book
    contact_book.delete_contract("Janez")
    print contact_book