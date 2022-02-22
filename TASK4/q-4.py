#checking the given number is a palindrome number or not
numb = input("enter the number to be checked: ")
reverse=numb[::-1]
if(numb==reverse):
    print(True)
else:
    print(False)