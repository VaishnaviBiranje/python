class mother:
    mothername = ""
    def mother(self):
        print(self.mothername)

class father:
    fathername = ""
    def fater(self):
        print(self.fathername) 

class son(mother,father):
    def parent(self):
        print("father name is : ",self.fathername)
        print("mother name is : ",self.mothername) 

s1 = son()
s1.fathername = "sunil"
s1.mothername = "sneha"
s1.parent()


