#1
year=int(input("Enter the year"))
if (year%4 == 0 and year%400 == 0 or year%100!= 0):
  	print("Entered year is a leap year")


#2
print("Enter length")
length = input()
print("Enter breadth")
breadth = input()
if length == breadth:
  print("Yes, it is square")
else:
  print ("No, it's Rectangle")


#3
print("Enter first age")
first = input()
print("Enter second age")
second = input()
print("Enter third age")
third = input()

if first >= second and first >= third:
 	 print ("Oldest is",first)
elif second >= first and second >= third:
  	print ("Oldest is",second)
elif third >= first and third >= second:
  	print ("Oldest is",third)
else:
  	print ("All are equal")



#4
points = input(“Enter point”)
if points <= 50:
    result = "Sorry! No prize this time."
elif points <= 150:
    result = "Congratulations! You won a wooden dog!"
elif points <= 180:
    result = "Congratulations! You won a book!"
else:
    result = "Congratulations! You won Chocolates!"

print(result)

#5
print("Enter quantity")
quantity = input()
if quantity * 100 > 1000:
    print("Cost is", ((quantity * 100) - (.1 * quantity * 100)))
else:
    print("Cost is", quantity * 100)






