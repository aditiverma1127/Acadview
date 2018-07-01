#1
radius=float(input("Enter the radius of circle"))
def area(radius):
  area_circle=3.14*radius*radius
  return area_circle
final_area=area(radius)
print("The area of the circle with the inserted radius is",final_area)

#2
#creating a method to determine whether a number is perfect or not
def perfect(n):
  sum = 0
  for i in range(1,n):
    if n%i == 0:
      sum = sum + i
  if sum == n:
    return True
  else:
    return False
#Calling method in for loop
for i in range(1,1001):
  if perfect(i):
    print (i)

#3
def table(n,i):
  print(n*i)
  i=i+1
  if i<=10:
    table(n,i)
table(12,1)

#4
#Using input statements
a=int(input("Enter the value of a"))
