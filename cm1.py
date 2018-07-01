
#1
class Circle():
def __init__(self,radius):
self.radius = radius
def  getArea(self):
return 3.14*self.radius*self.radius
def getCircumference(self):
return self.radius*2*3.14
  
radius = input(“Enter radius: ”)
cir=Circle(radius)
cir.getArea()

#2
class Student:
 def __init__(self,rollNo,age):
     self.rollNo=rollNo
     self.name=age
 def display(self):
   print(self.rollNo)
   print(self.name)

roll = input(“Enter roll number: ”)
name = input(“Enter name: ”)
s=Student(roll, name)
s.display()

#3
class Temperature():
    def  convertFahrenhiet(self,celsius):
        return (celsius * 9/5) + 32
    def convertCelsius(self,fahrenhiet):
        return (fahrenhiet - 32) * 5/9
temp=Temperature()
c = temp.convertFahrenhiet(100)
f = temp.convertCelsius(98.4)
print(c, f)


#4
class MovieDetails:
def __init__(self,name,artist,year,ratings):
        self.name=name
        self.artist=artist
        self.year=year
        self.ratings=ratings
   
 	def display(self):
print("The",self.name,"starring",self.artist,"has been released                     in",self.year,"with the ratings",self.ratings)

    	def update(self):
        name = input("Enter movie name: ")
        self.name = name
        artist = input("Enter artist name: ")
        self.artist = artist
        year = input("Enter year of release: ")
        self.year = year
        ratings = input("Enter ratings: ")
        self.ratings = ratings
        print("The",self.name,"starring",self.artist,"has been released in",self.year,"with the ratings",self.ratings)

movie=MovieDetails('IronMan','Robert Downey Jr',2008,7.9)
movie.display()
movie.update()


#5

class Expenditure:
    def __init__(self,savings,expenditure):
        self.savings=savings
        self.expenditure=expenditure
    def display_expense(self):
        print(self.expenditure)
        print(self.savings)
    def cal_salary(self):
        total = self.savings + self.expenditure
        print("The total salary is",total)
        
savings = input("Enter savings: ")
expen = input("Enter expenditure: ")
exp = Expenditure(savings, expen)
exp.display_expense()
exp.cal_salary()
