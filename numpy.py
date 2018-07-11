#question 1
import numpy as np
l=np.random.random((10,1))
m=np.mean(l)
print("mean is :",m)

#question 2
import numpy as np
arr=np.random.random((20,1))
v=np.var(arr)
s=np.std(arr)
print("variance is :",m)
print("standard deviation is :",s)

#question 3
import numpy as np
A=np.random.random((10,20))
B=np.random.random((20,25))
mul=A.dot(B)
print("after multiplication :",mul)
add=np.sum(mul)
print("after addition :",add)

#question 4
import numpy as np
import math
A=([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
np_arr=np.array(A)
l=[]

def f(ele):
    return (1/(1+math.exp(-ele)))
    
    
ar_B=np.array(list(map(f,np_arr)))

print("after mapping : ",ar_B)


