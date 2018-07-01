1. import time
    from threading import Thread
    def sleepMe(i):
    print("Thread %i going to sleep for 5 seconds." % i)
    time.sleep(5)
    print("Thread %i is awake now." % i)
    for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    	    th.start()


      2. import time
          from threading import Thread
          def sleepMe(i):
    print("Thread %i." % (i+1))
    time.sleep(1)
          for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()

3. import time
    from threading import Thread
    def sleepMe(i , B):
	    time.sleep(B)
	    print("Thread %i." % (i))
    
    a = [0, 6, 8, 9]
    B = 2 
    for i in a:
    th = Thread(target=sleepMe, args=(i,B , ))
    th.start()
    B+= 2 

4. import time
    from threading import Thread
    def func(n) : 
	fact = 1 
for i in range(1,n+1):
    fact = fact * i 
print(“fact“)
n = input()
th = Thread(target=func, args=(n, ))
th.start()



	




