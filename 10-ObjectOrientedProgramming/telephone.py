from contacts import Contact
from contacts_list import Contact_List
# Creating a Contact_List object
my_contacts = Contact_List()

# Adding contacts
contact1 = Contact("John Brown", "brown@onet.pl", "555234000")
contact2 = Contact("Anna May", "am@o2.pl", "232000199")
contact3 = Contact("George Small", "smallg@google.pl", "222999100")
contact4 = Contact("Paola Big", "bigpaola@poczta.pl", "100200300")

# Adding contacts to the list
my_contacts.add_contact(contact1)
my_contacts.add_contact(contact2)
my_contacts.add_contact(contact3)
my_contacts.add_contact(contact4)

# Displaying the contact list
print("Contact List:")
my_contacts.display_contacts()