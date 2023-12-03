class address:
    def __init__(self,number,street,city):
        self.number=number
        self.street=street
        self.city=city
        self.address={}

    def add_address(self):
        self.address['number']=self.number
        self.address['street']=self.street
        self.address['city']=self.city
        return self.address
    
    def show_info(self):
        print(f'address is: {self.number}\t\t{self.street}\t\t{self.city}')

class person:
    def __init__(self,id,name,family,mobile,email):
        self.id=str(id)
        self.name=name
        self.family=family
        self.mobile=mobile
        self.email=email
        self.person={}

    def add_person(self):
        self.person['id']=self.id
        self.person['name']=self.name
        self.person['family']=self.family
        self.person['mobile']=self.mobile
        self.person['email']=self.email
        return self.person
    
    def show_info(self):
        print(self.id+" "+self.name+ " "+self.family+" "+self.mobile+" "+self.email)


class Contact(person,address):
    def __init__(self,id,name,family,mobile,email,number,street,city):
        person.__init__(self,id,name,family,mobile,email)
        address.__init__(self,number,street,city)
        self.contact={}

    def add_person_address(self):
        dic1=self.add_person()
        dic2=self.add_address()
        for i in (dic1,dic2):
            self.contact.update(i)
        return self.contact
    
    def show_info(self):
        person.show_info(self)
        address.show_info(self)

    
class phone_book:
    def __init__(self):
        self.phone_book=[]

    def add_contact_to_phonebook(self,x_dic):
        self.phone_book.append(x_dic)
        return self.phone_book
    
    def show_info(self):
        for i in self.phone_book:
            for key,value in i.items():
                print(key,':',value,end=' ')
            print()


c1=Contact(1001,'Sara','Parker','001-1111111','aaa@gmail.com','10','Ca','LosAngles')
x_dic1 = c1.add_person_address()

phonbook1=phone_book()
phonbook1.add_contact_to_phonebook(x_dic1)
phonbook1.show_info()
