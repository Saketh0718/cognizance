import numpy as np
l1=list(input("Please Enter First array: ")) 
array1=np.array(l1)
l2=list(input("Please Enter Second array: "))
array2=np.array(l2)
print(np.array_equal(array1,array2))