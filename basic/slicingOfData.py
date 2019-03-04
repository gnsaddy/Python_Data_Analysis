import pandas as pd

testDict = {
    'Name' : ['Aditya','Alok','Amit','Syed','Tanya','Bhaskar','Akash'],
    'Age' : [21,20,23,22,21,20,21],
    'Address':['Banglore','Banglore','Delhi','Delhi','Delhi','Kolkata','Mysore']
}

df = pd.DataFrame(testDict)
# head() is used to print lines from starting with the argument as line count
print(df)
print("\n", df.head(3))

# tail() is ued to print lones from end with the argument as line count

print("\n",df.tail(2))
