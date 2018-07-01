#1
t=('hi','hello','python','django')
print(" tuple is",t)
print("length of the tuple is",len(t))

#2creating a tuple
t=(58,64,886,998,170,162)
#Finding maximum element
print(" maximum element ",max(t))
print("minimum element ",min(t))

#3
t=(1,4,6,9,10,12)
pro=(1*4*6*9*10*12)
print(" product ",pro)

days=set(["mon","Tue","Wed","Thur","Fri","Sat","Sun"])
values=set(['mon','Sun','Wed','Sat'])
print(" first set is",days)
print("set is",values)

#Difference of two sets Creating a set
days=set(["mon","Tue","Wed","Thur","Fri","Sat","Sun"])
values=set(['mon','Sun','Wed','Sat'])
#Displaying set
print(" set ",days)
print("set is",values)

#Difference between two sets
differ_set=days-values
print("The difference ",differ_set)

#Comparing two sets

days=set(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
values=set(['Monday','Sunday','Wednesday','Saturday'])
#Displaying sets
print("The first set is",days)
print("The first set is",values)

#Comparing two sets
t_set=days<=values
print("the comparison of two sets is",t_set)


#Intersection of two sets
#Creating a set
days=set(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
values=set(['Monday','Sunday','Wednesday','Saturday'])
#Displaying sets
print("The first set is",days)
print("The first set is",values)

#Intersection of two sets
combined_set=days&values
print(" intersecti",combined_set)


#Creating dictionaries
student={
'juhi':89,
'hira':80,
'sant':95,
'sarita':79,
'priya':99
}
#Displaying values
print("The marks dictionary is",student)

2. #Sort the dictionary

student={
'juhi':89,
'hira':80,
'sant':95,
'sarita':79,
'priya':99
}
#Displaying values
print("The marks dictionary is",student)

#Sort the dictionary
for key in sorted(student):
   print("%s: %s" % (key, student[key]))

sort(dict.keys())

#3

s='MISSISSIPPI'
#converting string to lists
l=list(s)
m_count=l.count('M')
i_count=l.count('I')
s_count=l.count('S')
p_count=l.count('P')
#creating final dictionary
dict={
    'M':m_count,'I':i_count,'S':s_count,'P':p_count
}
print("dictionary ",dict)


