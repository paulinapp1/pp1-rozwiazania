from contacts import Contact

class Contact_List:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name} Email: {contact.email} Telephone: {contact.telephone}")