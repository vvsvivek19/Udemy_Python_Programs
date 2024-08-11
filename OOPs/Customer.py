class Customer:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    def get_name(self):
        print('Customer Name:',self.name)
    def get_phone(self):
        print('Phone Number:',self.phone)
    def set_phone(self,new_phone):
        self.phone = new_phone

c1 = Customer('Vivek',8604419397)
c1.get_name()
c1.get_phone()
c1.set_phone(9935680323)
c1.get_phone()