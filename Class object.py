#A class is a blueprint or design that defines the variables and the methods common to all objects of a certain kind
# The data stored in its variables is known as attributes or the fields
# The code that can access this data to give the necessary output are called methods or functions
#empty Class = a class which do not having any attributes or methods
class car:
    pass
#object of the class
obj = car()  #object Created
#Cfeate the variables/attributes of class
obj.name = "Rolls Royce"
obj.color = "Black"
print(obj.name,obj.color)

#class
class student:
    Name = "Chirag"
    rNo  = 69
obj = student()
print(obj.Name, obj.rNo)

class student:
    name = None
    rNo  = None
obj = student()
name = input("enter name of student:")
obj.name = name
rollNo = int(input("rollNo:"))
obj.rNo = rollNo


class student:
    name = None
    rNo  = None
    def studentDetail(self):
        name = "Abhi"
        rNo  = 22
        return(name,rNo)
obj = student()
print(obj.studentDetail())

class book:
    ISBN = None
    Title = None
    Author = None
    NoofPages = None
    publisher = None
    def bookDetail(self):
        ISBN = int(input("ISBN:"))
        Title = input("Enter name of book:")
        Author = input("Enter name of author:")
        NoofPages = int(input("NoofPages:"))
        publisher = input("publisher:")
        return(ISBN,Title,Author,NoofPages,publisher)
obj = book()
NoofBooks = int(input("Enter NoofBooks to take the details: "))
for i in range(NoofBooks):
    print(obj.bookDetail())


class student:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
stud1 = student("Abc","12","abc@gmail.com")
print("stud1 details:", stud1.name,stud1.age,stud1.email)




class student:
    name = None
    age=None
    phoneNumber = None
    email = None
    def getStudentDetails(self):
        self.name = input("Enter name :")
        self.age = int(input("Enter age in interger : "))
        self.phoneNumber = int(input("Enter Phone Number : "))
        self.email = input("Enter E--mail id : ")
    def setStudentDetails(self):
        name = self.name
        age = self.age
        phoneNumber = self.phoneNumber
        email = self.email
    print("Name : ", name, "\n", "age : ", age, "phone number : ", phoneNumber, "\n", "Email : ", email)
obj1 = student()
obj1.getStudentDetails()
obj1.setStudentDetails()