class person():
    def __init__(self,name,age):
         self.name=name
         self.age=age

    def display(self):
         print(self.name,self.age)

class student(person):
     def __init__(self,name,age,dob):
          self.sname=name
          self.sage = age
          self.dob =dob
          super().__init__("rahul",age)

     def display(self):
           print(self.name,self.age,self.dob)

obj =student("vaishnavi",20,"15-10-2004")
obj.display()
