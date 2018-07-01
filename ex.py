#1 
<ipython-input-2-eacf31491228> in <module>()
      1 a=3
      2 if a<4:
	3     a=a/(a-3)
      4     print(a)
try :
    a = 3
    if a < 4 :
        b = a/(a-3)
   
    print ("Value of b = ", b)
 

except(ZeroDivisionError, NameError):
    print ("\nError Occurred and Handled")
#2
<ipython-input-6-ea9ef666f953> in <module>()
      1 l=[1,2,3]
----> 2 print(l[3])

a = [1, 2, 3]
try:
   print ("Second element = %d" %(a[1]))
 
   print( "Fourth element = %d" %(a[3]))
except IndexError:
   print ("An error occurred")




#3
<ipython-input-11-deeb71e90084> in <module>()
      1 
      2 try:
----> 3    raise NameError("Hi there")  # Raise Error
      4 except NameError:
      5    print ("An exception")

#4


-5.0
a/b result in 0


#5
l=[1,2,3,4]
try:
   print("The fourth element",l[4])
except Exception as e:
   print("List index out of range")

s='gh'
try:
   print(int(s))
except Exception as e:
   print("Value error handled")
try: 
    from _foo import * 
except ImportError: 
    raise ImportError('<any message you want here>')

#6
class Error(Exception):
    """Base class for other exceptions"""
    pass
 
class AgeTooSmallError(Error):
    """Raised when the entered age is smaller than 18"""
    pass
 
while True:
    try:
        age =  input("Enter Age: ")
        if age < 18:
            raise AgeTooSmallError
        break
    except AgeTooSmallError:
        print("The entered Age is too small, try again!")
        print('')
    
        
print("You entered the appropriate age value!")





