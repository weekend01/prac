import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
file_path = r"C:\Users\ASUS\Desktop\DSML_practical\Lipstick.csv"  # Use the uploaded file path
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

# Define the test data: [Age < 21, Income = Low, Gender = Female, Marital Status = Married]
test_data = pd.DataFrame([[0, 0, 1, 1]], columns=['Age', 'Income', 'Gender', 'Ms'])

# Make a prediction using the trained model
prediction = clf.predict(test_data)

# Display the result
if prediction[0] == 1:
    print("\nPrediction: The customer will buy the lipstick (Yes).")
else:
    print("\nPrediction: The customer will not buy the lipstick (No).")


# A DataFrame in pandas is a two-dimensional, tabular data structure, similar to an Excel spreadsheet or SQL table. It consists of rows and columns, where:

# Rows: Represent individual data points or records.
# Columns: Represent features, attributes, or variables.


# pip install pandas,pip install scikit-learn




# The DecisionTreeClassifier is a class in the scikit-learn library, used for building decision tree models for classification tasks. A decision tree is a flowchart-like structure where:

# Nodes: Represent decisions or tests on features.
# Edges: Represent outcomes of those decisions/tests.
# Leaves: Represent the predicted classes.
# How DecisionTreeClassifier Works
# The algorithm splits the data into subsets based on feature values, aiming to maximize information gain or minimize impurity (such as Gini Impurity or Entropy). The goal is to create the most "pure" leaf nodes, where each node ideally contains examples of only one class.