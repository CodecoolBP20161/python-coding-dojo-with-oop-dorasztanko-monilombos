

# Step 1
class Contact:
    # Step 2
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

# Step 3
    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = []


# Step 4
class Supplier(Contact):
    # Step 5
    all_orders = {}

    def __inti__(self, item):
        super(Contact, self).__init__(name, email)
        self.item = item

    # @classmethod
    # def order(cls):



# contact = Contact('Moni', 'moni@net.hu')
# contact2 = Contact('Dori', 'dori@net.hu')
# print(contact.name)
# print(Contact.all_contacts)
# Contact.reset_contacts()
# print(Contact.all_contacts)
