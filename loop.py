#1
i=0
while(i<100):
  num=input("enter the number")
  print(num)
  i=i+1
#2
while True:
  print ("INFINITE")

#3
#Defining an empty list
numbers=[]
for i in range(0,5):
  num=int(input("Enter the number"))
  numbers.append(num)
print("The list is",numbers)
#defining an empty list for squares
  
squares=[]
for num in numbers:
    sq=num*num
    squares.append(sq)
print("The list of squares is",squares)  


#4
l=[1,'abc',2.0,2,'def',3.0]
for i in l:
  print("The type of",i,"is",str(type(i)))


#5
   even=[]
   odd=[]
for i in range(1,101):
  if i%2 == 0:
    even.append(i)
  else:
      odd.append(i)
print(“The list for even numbers is”,even)
print(“The list for odd numbers is”,odd)

#6
i = 1
while i<=4:
  print ("*"*i)
  i = i+1

#7

   dict={
    'Aditi':101,
    'tom':102,
    'priya':103
}

for key in dict.keys():
  print(key,dict[key])
  
#8
list=['roti','daal','Jamun','rice','chole']
name=input("Enter the food name")
for con in list:
  if con==name:
    print("Found")
    li.remove(con)












