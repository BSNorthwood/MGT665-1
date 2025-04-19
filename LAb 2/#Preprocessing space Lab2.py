#Preprocessing space Lab2
import pandas as pd
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df = pd.read_csv('Students_Grading_Dataset.csv', low_memory = False) #load in the dataset

# Drop column 'column_name'
df.drop(columns=['Email'], inplace=True) #fairly useless, dropping because it resembles Student_ID in function

df['Gender'] = label_encoder.fit_transform(df['Gender']) #Encoding Gender
df['Department'] = label_encoder.fit_transform(df['Department']) #Encoding Department
df['Family_Income_Level'] = label_encoder.fit_transform(df['Family_Income_Level']) #Enconding Family_Income_Level
df['Parent_Education_Level'] = label_encoder.fit_transform(df['Parent_Education_Level']) #Encoding Parent_Education_Level
df['Internet_Access_at_Home'] = label_encoder.fit_transform(df['Internet_Access_at_Home']) #Encoding_Acess_at_Home
df['Extracurricular_Activities'] = label_encoder.fit_transform(df['Extracurricular_Activities']) #Encoding Extracirricular_Activities
grade_to_numeric = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0} #Setting what grade letters will become
df['Grade'] = df['Grade'].map(grade_to_numeric) #Changing the kind of values in the column
df.to_csv("Students_Grade.csv", index=False) #Saving the new Dataset
print(df.head())  # Display the first few rows

