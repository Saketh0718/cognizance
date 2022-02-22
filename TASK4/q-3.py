numb = int(input("Enter The Number of Students : "))
temp = [['Roll No','Name','Marks']]
for i in range(numb):
    roll_no = input('Enter Roll No : ')
    student_name = input('Enter Student Name : ')
    marks = int(input('Enter Marks : '))
    temp.append([roll_no,student_name,marks])
for i in range(len(temp)):
    for j in range(len(temp[i])):
        k=temp[i][j]
        print(k,end='\t')
    print('\n')
h=int(input('Enter The Row to be Printed : '))
for i in temp[h]:
    print(i,end='\t')
