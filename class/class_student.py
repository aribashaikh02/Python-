#creating class
class Student:
    def __init__(self,name,age):
        self.name= name
        self.age= age

 #creating multiple objects
s1= Student ("Ariba",18)
s2= Student ("Samir",19)

#displaying details with descriptions
print(f"Student 1:\n Name:{s1.name}\n Age:{s1.age}\n")
print(f"Student 2:\n Name:{s2.name}\n Age:{s2.age}\n")
