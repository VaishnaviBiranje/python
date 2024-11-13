class Base:
    def __init__(self,name):
        self.name=name

    def getname(self):
        return self.name
    
class child(Base):
    def __init__(self,name,age):
        Base.__init__(self,name)
        self.age=age

    def getAge(self):
        return self.age
    
class Grandchild(child):
    def __init__(self,name,age,address):
        child.__init__(self,name,age)
        self.address=address

    def getAddress(self):
        return self.address  
      
g = Grandchild("vaishnavi",20,"noida")
print(g.getname(),g.getAge(),g.getAddress()) 

                        