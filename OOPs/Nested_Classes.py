class Customer:

    def __init__(self, id, name, bdno,bstreet,bcity,bcountry,bpin,sdno,sstreet,scity,scountry,spin):
        self.custID = id
        self.custName = name
        self.baddr = self.Address(bdno,bstreet,bcity,bcountry,bpin)
        self.saddr = self.Address(sdno,sstreet,scity,scountry,spin)

    class Address:
        def __init__(self,dno,street, city, country,pin):
            self.dno = dno
            self.street = street
            self.city = city
            self.country = country
            self.pin = pin
        def display(self):
            print(self.dno)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin)
c = Customer(10, 'Vivek', '39B','Ganga Nagar, Saraswati Vihar','Kanpur','India',208015,'39B','Ganga Nagar, Saraswati Vihar','Kanpur','India',208015)

c.saddr.display()
