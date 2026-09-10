class Flipkart:
    discount = 30

    def info(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print('Welcome', self.name)

    @classmethod
    def updatediscount(cls):
        cls.discount = 40
        print("Updated Discount:", cls.discount)

    @staticmethod
    def contact_support():
        print("Contact Flipkart support")

lohitha = Flipkart()
usharani = Flipkart()
teja = Flipkart()