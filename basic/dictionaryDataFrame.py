import pandas as pd

testDict = {
    'Name' : ['Aditya','Alok','Amit','Syed','Tanya','Bhaskar','Akash'],
    'Age' : [21,20,23,22,21,20,21],
    'Address':['Banglore','Banglore','Delhi','Delhi','Delhi','Kolkata','Mysore']
}

df = pd.DataFrame(testDict)
print(df)
