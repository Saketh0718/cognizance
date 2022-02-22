#pattern of triangle
numb=int(input("enter the number of rows: "))
for i in range(numb):
    for j in range(numb-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
