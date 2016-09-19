

# Step 6
class ContactList(list):

    # Step 7
    @staticmethod
    def search(contact):
        return [element for element in Contact.all_contacts if contact in element.name]

    # Step 8
    @staticmethod
    def longest_name():
        try:
            return max([element.name for element in Contact.all_contacts], key=len)
        except ValueError:
            return None


# Step 1
class Contact(object):
    # Step 2
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


# Step 3
    @classmethod
    def reset_contacts(cls):
        if cls.all_contacts is None:
            pass
        else:
            while cls.all_contacts:
                for element in cls.all_contacts:
                    cls.all_contacts.remove(element)


# Step 4
class Supplier(Contact):
    # Step 5
    all_orders = {}

    def order(self, item):
        if self.name in Supplier.all_orders.keys():
            Supplier.all_orders[self.name].append(item)
        else:
            Supplier.all_orders.update({self.name: [item]})


# supplier2 = Supplier('Moni', 'moni@net.hu')
# contact2 = Contact('Dori', 'dori@net.hu')
# # print(Contact.all_contacts)
# Contact.reset_contacts()
# # print(Contact.all_contacts)
# supplier = Supplier('Anna', 'anna@net.com')
# supplier3 = Supplier('Anna', 'anna@net.com')
# supplier4 = Supplier('Aurélia', 'aurelia@net.com')
# supplier3.order('kiscica')
# # print(supplier.name)
# supplier.order('alma')
# supplier2.order('kréta')
# supplier.order('körte')
# supplier.order('kréta')
# print(Supplier.all_orders)
# print(Contact.all_contacts.search('Anna'))
# print(Contact.all_contacts.longest_name()))
