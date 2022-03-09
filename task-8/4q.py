import pandas as pd
ser=pd.Series(['amrita','school','of','engineering','chennai' ,'campus'])
A=ser.str.capitalize()
for B in A:
    print(B,end=" ")

