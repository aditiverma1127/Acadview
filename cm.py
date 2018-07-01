
#1
The time module
This module provides a number of functions to deal with dates and the time within a day. It’s a thin layer on top of the C runtime library.

A given date and time can either be represented as a floating point value (the number of seconds since a reference date, usually January 1st, 1970), or as a time tuple.

Getting the current time
Example: Using the time module to get the current time
# File: time-example-1.py

import time

now = time.time()

print now, "seconds since", time.gmtime(0)[:6]
print
print "or in other words:"
print "- local time:", time.localtime(now)
print "- utc:", time.gmtime(now)

937758359.77 seconds since (1970, 1, 1, 0, 0, 0)

or in other words:
- local time: (1999, 9, 19, 18, 25, 59, 6, 262, 1)
- utc: (1999, 9, 19, 16, 25, 59, 6, 262, 0)
The tuple returned by localtime and gmtime contains (year, month, day, hour, minute, second, day of week, day of year, daylight savings flag), where the year number is four digits, the day of week begins with 0 for Monday, and January 1st is day number 1.

Converting time values to strings
You can of course use standard string formatting operators to convert a time tuple to a string, but the time module also provides a number of standard conversion functions:

 
Example: Using the time module to format dates and times
# File: time-example-2.py

import time

now = time.localtime(time.time())

print time.asctime(now)
print time.strftime("%y/%m/%d %H:%M", now)
print time.strftime("%a %b %d", now)
print time.strftime("%c", now)
print time.strftime("%I %p", now)
print time.strftime("%Y-%m-%d %H:%M:%S %Z", now)

# do it by hand...
year, month, day, hour, minute, second, weekday, yearday, daylight = now
print "%04d-%02d-%02d" % (year, month, day)
print "%02d:%02d:%02d" % (hour, minute, second)
print ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")[weekday], yearday

Sun Oct 10 21:39:24 1999
99/10/10 21:39
Sun Oct 10
Sun Oct 10 21:39:24 1999
09 PM
1999-10-10 21:39:24 CEST
1999-10-10
21:39:24
SUN 283


#2
import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

#3
import datetime
a = '2010-01-31'
d = datetime.datetime.strptime(a, "%Y-%m-%d")
print(“The month is”,d.month)

Or

import datetime
d = datetime.date.today()
print(d.month)


#4	
import datetime
a = '2010-01-31'
d = datetime.datetime.strptime(a, "%Y-%m-%d")
print(“The day is:”d.day)

Or

import datetime
d = datetime.date.today()
print(d.day)


#5
import datetime
a = '2011-01-11'
d = datetime.datetime.strptime(a, "%Y-%m-%d")
print(“The day is:”d.day)	

#6
import time
print ("Time is",time.localtime())

#7
import math
num=int(input("Enter the number"))
print ("The factorial of entered number is : ", end="")
print (math.factorial(num))

#8
import math
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
print(math.gcd(num1,num2))

#9
import os
            print(os.getcwd())
    
           import os 
           os.environ	
            
