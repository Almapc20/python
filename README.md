# python
python experience

If you create an instance of a class, you cannot assign it directly to a list or dictionary
For example, we create an instance of the Contact class called Contact 1
--------------------------------------------------------------------------------------------
class Contact(person,address):
    def __init__(self,id,name,family,mobile,email,number,street,city):
---------------------------------------------------------------------------------------------
c1=Contact(1001,'Sara','Parker','001-1111111','aaa@gmail.com','10','Ca','LosAngles')

if you want use c1 for print informathin you must convert C1 to dict

For this, we must define a function in the contact class that reads information from two parent classes and stores it in two different dictionaries.
Then we can update these two dictionaries together.
for example:


 def add_person_address(self):
        dic1=self.add_person()
        dic2=self.add_address()
        for i in (dic1,dic2):
            self.contact.update(i)
        return self.contact
