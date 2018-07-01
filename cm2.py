
#1
class Animal:
   def animal_attributes(self,legs):
       print("Animals have",legs,"legs")
#Inheriting class Animal
class Tiger(Animal):
   def tiger_atrributes(self,nutrition):
       print("Tiger is",nutrition)
tig=Tiger()
tig.animal_attributes(4)
tig.tiger_atrributes('carnivores')

#2
A B
A B

#3
class Cop:
   def __init__(self,name,experience,):
       self.name=name
       self.experience=experience
   def display_details(self):
       print(self.name,"cop is on duty with",self.experience,"years of experience")
   def update_details(self):
       self.name='Sherlock'
       self.experience=7
class Mission(Cop):
   def __init(self):
       super(Mission,self).__init()
   def display_mission(self,mission):
       print("The active mission is",mission)

   def assign_cop(self,mission):
       print(self.name,"has been assigned",mission)
mission=Mission('Sherlock',4)
mission.display_mission('Secret')
mission.display_details()
mission.assign_cop('Secret')
#4
class Shape:
   def __init__(self,length,breadth):
       self.length=length
       self.breadth=breadth
   def area(self):
       print("The area is",self.length*self.breadth,"units")

class  Rectangle(Shape):
   def __init__(self):
       super(Rectangle,self).__init__()
class Square(Shape):
   def __init__(self):
       super(Square,self).__init__()
rect=Shape(2,4)
rect.area()
sq=Shape(4,4)
sq.area()
