import pandas as pd
import numpy as np

# list with values
names = ['Aditya Raj','Alok Tripathi','Amit Rawat','Adarsh Tripathi','Bhaskar Uday','Syed Numan']

# list to Series() object

ser = pd.Series(names)

print(ser)
print(ser.index)

rolls = [101,102,103,104,105,106]

ser1 = pd.Series(rolls)
print(ser1)

registration = [True,False,False,True,True,False]

ser2 = pd.Series(registration)
print(ser2)