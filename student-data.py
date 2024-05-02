import pandas as pd

#create dataframe
studentData = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'], 'Age': [25, 30, 35, 40, 45], 'Grade': [88, 92, 85, 90, 95]}
studentData = pd.DataFrame(studentData)
print(studentData)

# write to csv
studentData.to_csv('studentdata.csv')

# read and print top 3
studentDataFrame = pd.read_csv('studentdata.csv')
print(studentDataFrame.head(3))

# diplay age column
age = studentData['Age']
print(age)

# students with grades > 80
topGrades = studentData.loc [(studentData.Grade >= 80)]
print(topGrades)