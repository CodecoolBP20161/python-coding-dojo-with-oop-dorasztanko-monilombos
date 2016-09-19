# Step 1
class Contact(object):
    # Step 2
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    # def __str__(self):
    #     return self.name
    #
    # def __repr__(self):
    #     return self.name


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
        # for value in Supplier.all_orders.values():
        #     print(value)
        if self.name in Supplier.all_orders.keys():
            Supplier.all_orders[self.name].append(item)
        else:
            Supplier.all_orders.update({self.name: [item]})


supplier2 = Supplier('Moni', 'moni@net.hu')
# print(contact)
# contact2 = Contact('Dori', 'dori@net.hu')
# print(contact.name)
# print(contact.email)
# print(Contact.all_contacts)
# Contact.reset_contacts()
# print(Contact.all_contacts)
supplier = Supplier('Anna', 'anna@net.com')
# print(supplier.name)
supplier.order('alma')
supplier2.order('kréta')

supplier.order('körte')
# supplier.order('kréta')
print(Supplier.all_orders)




