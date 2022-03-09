import numpy as np
in1=int(input("Enter Initial number: "))
in2=int(input("Enter Last number:"))
i=np.arange(in1,in2+1)
array1 = np.array(i)
print("Array created by the user is: ",i)
a= np.zeros([len(array1)+(len(array1-1)*4)])
a[::6]=array1
print(a)


