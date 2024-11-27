import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\ASUS\Desktop\DSML_practical\IRIS.csv" # Uploaded file path
df = pd.read_csv(file_path)

# Display the dataset
print("Dataset Head:")
print(df.head())

# 1. List down the features and their types
print("\nFeature Types:")
for column in df.columns:
    if df[column].dtype == 'object':
        print(f"{column}: Nominal")
    else:
        print(f"{column}: Numeric")

# 2. Create histograms for each feature
print("\nCreating histograms for each feature...")
for column in df.columns[:-1]:  # Exclude the target column if it's not numeric
    plt.figure(figsize=(8, 6))
    plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.show()
