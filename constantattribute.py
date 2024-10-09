class student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age

s=student("vaishnavi",109,20)
print(getattr(s,'name'))   
print(getattr(s,'id')) 
print(getattr(s,'age'))  


setattr(s,"age",23)
print(getattr(s,'age'))

print(hasattr(s,'id'))

print(s.__doc__)
print(s.__dict__)
print(s.__module__)
