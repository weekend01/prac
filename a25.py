import pandas as pd

# Step 1: Load the dataset
# Correct the file path by using a raw string or escaping backslashes
file_path = r"C:\Users\rutuj\OneDrive\Desktop\DSML\cleaned_sample_data.csv"  # Use raw string
# Alternatively:
# file_path = "C:\\Users\\rutuj\\Downloads\\Datasets\\Datasets\\Lipstick.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Step 2: Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Display basic info about the dataset
print("\nDataset Info:")
print(df.info())

# Step 4: Handle missing values
# Fill missing numerical values with the column mean
numerical_cols = df.select_dtypes(include=["float64", "int64"]).columns
df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())
# df.select_dtypes(include=["float64", "int64"]): Selects all numerical columns.
# df[numerical_cols].mean(): Calculates the mean of each numerical column.
# df[numerical_cols].fillna(...): Fills missing values (NaN) in the numerical columns with their respective means.
# Purpose: Ensures no missing values in numerical columns by replacing them with the average.


# Fill missing categorical values with the most frequent value
categorical_cols = df.select_dtypes(include=["object"]).columns
df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])
# df.select_dtypes(include=["object"]): Selects all categorical columns (columns with string-like values).
# df[categorical_cols].mode(): Calculates the most frequent value (mode) for each categorical column.
# .iloc[0]: Ensures the mode is extracted as a scalar value.
# Purpose: Replaces missing values in categorical columns with their mode.


# Step 5: Remove duplicates
df = df.drop_duplicates() #df.drop_duplicates(): Removes any duplicate rows in the dataset

# Step 6: Rename columns for clarity
df.rename(columns=lambda x: x.strip().replace(" ", "_").lower(), inplace=True)
# Lambda Function: A shorthand to process each column name.
# x.strip(): Removes leading and trailing spaces.
# x.replace(" ", "_"): Replaces spaces in column names with underscores (_).
# x.lower(): Converts all column names to lowercase.
# inplace=True: Applies the changes directly to the DataFrame.


# Step 7: Save cleaned data to a new CSV file
cleaned_file_path = "cleaned_sample_data.csv"
df.to_csv(cleaned_file_path, index=False)

# Final Output
print("\nCleaned Dataset:")
print(df.head())
print(f"\nCleaned dataset saved to {cleaned_file_path}")
