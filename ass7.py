import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
file_path = r"C:\Users\91830\Downloads\Lipstick.csv"  # Use the uploaded file path
df = pd.read_csv(file_path)

# Display the dataset
print("Dataset:")
print(df.head())

# Encode categorical features into numerical values
df['Age'] = df['Age'].map({'<21': 0, '21-35': 1, '>35': 2})  # Encoding for Age
df['Income'] = df['Income'].map({'Low': 0, 'Medium': 1, 'High': 2})  # Encoding for Income
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})  # Encoding for Gender
df['Ms'] = df['Ms'].map({'Single': 0, 'Married': 1})  # Encoding for Marital Status
df['Buys'] = df['Buys'].map({'No': 0, 'Yes': 1})  # Encoding for Buys (target variable)

# Features (input columns) and target (output column)
X = df[['Age', 'Income', 'Gender', 'Ms']]  # Features
y = df['Buys']  # Target

# Train the decision tree model
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Define the test data: [Age > 35, Income = Medium, Gender = Female, Marital Status = Married]
test_data = pd.DataFrame([[2, 1, 1, 1]], columns=['Age', 'Income', 'Gender', 'Ms'])

# Make a prediction using the trained model
prediction = clf.predict(test_data)

# Display the result
if prediction[0] == 1:
    print("\nPrediction: The customer will buy the lipstick (Yes).")
else:
    print("\nPrediction: The customer will not buy the lipstick (No).")
