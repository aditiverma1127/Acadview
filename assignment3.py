#question1
list=[]
x=int(input("enter first element"))
y=int(input("enter second number"))
z=int(input("enter third number"))
list.append(x)
list.append(y)
list.append(z)
print(list)

#question2
list.append("google")
list.append("apple")
list.append("facebook")
list.append("microsoft")
list.append("tesla")

#question3
l=[2,2,3,4,5,2]
l.count(2)

#question4
l=[2,7,6,5]
l.sort()
print(l)

#question5
l1=[4,5,6]
l2=[1,7,8]
l3=[]
l3.extend(l1)
l3.extend(l2)
l3.sort()
print(l3)

#question6
l=[1,2,3,4,5]
print("implementing stack")
l.append(6)
l.pop()
print(l)

print("implementing queue")
l.append(7)
l.pop(0)
print(l)
