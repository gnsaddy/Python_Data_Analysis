import pandas as pd
import numpy as np

student_name_USN = {'Aditya':'1RD18MCA01','Akash':'1RD18MCA02','Ajit':'1RD18MCA03','Ajay':'1RV18MCA03'}
ser1 = pd.Series(student_name_USN)
print(ser1)

student_name_age = {'Aditya':21,'Akash':20,'Ajit':20,'Ajay':21}
ser2 = pd.Series(student_name_age)
print(ser2)

print(ser1[3])