class Contact:
    all_contacts = []
   
    def __init__(self, name,email):
        self.name = name
        self.email=email
    def test(self):
        super().test()
        print("contact")
        
   
class AddressHolder:
    def __init__(self, street):
        self.street = street

    def test(self):
        
        print("Hello")
     

class Friend(Contact, AddressHolder):
    def __init__(self, phone,name,email,street):
        
        self.phone = phone
        #Contact.__init__(self,name,email)
        #AddressHolder.__init__(self,street)
    def test(self):
        print("FRIEND")
        super().test()

f1= Friend("123","John","john@gmail.com","street1")
f1.test()


