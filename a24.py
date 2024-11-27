import pandas as pd
import numpy as np
import openpyxl

# Load dataset
file_path = r"C:\Users\ASUS\Desktop\DSML_practical\Lipstick.csv"
df = pd.read_csv(file_path)

# Count unique values and data types
print("\nUnique values:\n", df.nunique())
print("\nData types:\n", df.dtypes)

# Convert floats with whole numbers to int, ints to str
df.update(df.select_dtypes('float64').apply(lambda x: x.astype('int64') if (x % 1).eq(0).all() else x))
# df.select_dtypes('float64'): Selects all columns with float64 data type.
# Lambda Function:
# x.astype('int64'): Converts a column to integers if all values are whole numbers (x % 1 == 0).
# (x % 1).eq(0).all(): Checks if all values in the column are whole numbers.
# df.update(): Updates the DataFrame df with the transformed data.


df[df.select_dtypes('int64').columns] = df.select_dtypes('int64').astype('str')
# df.select_dtypes('int64'): Selects all columns with int64 data type.
# .astype('str'): Converts the selected columns to strings.
# df[...] = ...: Explicitly assigns the transformed columns back to the DataFrame.
# Purpose: Standardize integer columns as strings for consistency.


# Handle missing values: Fill numerical with mean, categorical with mode
df.fillna({col: df[col].mean() for col in df.select_dtypes(['float64', 'int64'])}, inplace=True)
# df.select_dtypes(['float64', 'int64']): Selects all numerical columns.
# Dictionary Comprehension:
# Iterates through numerical columns (col).
# Computes the mean for each column (df[col].mean()).
# Creates a dictionary where keys are column names, and values are their respective means.
# fillna(): Replaces missing values (NaN) in these columns with their computed means.
# inplace=True: Modifies the DataFrame directly.


df.fillna({col: df[col].mode()[0] for col in df.select_dtypes(['object'])}, inplace=True)
# df.to_csv(): Writes the cleaned DataFrame df back to a CSV file.
# index=False: Omits row indices in the saved file to match the original format.


# Save cleaned data
df.to_csv(r"C:\Users\ASUS\Desktop\DSML_practical\Lipstick.csv", index=False)
print("\nCleaned data saved successfully!")
