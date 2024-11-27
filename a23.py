import pandas as pd
import numpy as np
import openpyxl


# pip install openpyxl


# Sample dataset based on the provided table
file_path = r"C:\Users\ASUS\Desktop\DSML_practical\Age Table.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Function to calculate entropy
def entropy(class_column):
    # Calculate the probabilities of each class
    prob = class_column.value_counts(normalize=True)
    # Calculate the entropy
    return -np.sum(prob * np.log2(prob))

# Step 1: Calculate the entropy of the whole dataset
total_entropy = entropy(df['Class'])
print(f"Total Entropy of the dataset: {total_entropy}")

# Step 2: Split the data based on the 'Age' column
age_groups = df.groupby('Age')

# Step 3: Calculate the entropy for each subset and their weighted average entropy
weighted_entropy = 0
for age, group in age_groups:
    group_entropy = entropy(group['Class'])
    weight = len(group) / len(df)  # Weight is the proportion of the group
    weighted_entropy += weight * group_entropy
    print(f"Entropy for Age = {age}: {group_entropy}")

# Step 4: Calculate the Information Gain
information_gain = total_entropy - weighted_entropy
print(f"\nInformation Gain for 'Age': {information_gain}")




# Information Gain=Total Entropy−Weighted Entropy
# Total Entropy: Uncertainty before splitting by Age.
# Weighted Entropy: Remaining uncertainty after splitting by Age.
