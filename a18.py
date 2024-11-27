import pandas as pd

# Load the dataset
file_path = r"C:\Users\ASUS\Desktop\DSML_practical\House Data.csv"  # Replace with the correct file path
df = pd.read_csv(file_path)

# Display the first few rows to understand the structure of the data
print("Dataset Preview:")
print(df.head())

# Define the categorical and quantitative variables
categorical_variable = 'district'  # Example: district or region
quantitative_variable = 'price'  # Example: house price

# Ensure the columns exist in the dataset
if categorical_variable in df.columns and quantitative_variable in df.columns:
    # Clean the quantitative variable column to remove non-numeric characters
    # Remove currency symbols and commas, and convert to numeric
    df[quantitative_variable] = (
        df[quantitative_variable]
        .str.replace(r"[^\d.]", "", regex=True)  # Remove non-numeric characters
        .astype(float)  # Convert to numeric
    )
    
    # Drop rows with missing or invalid values in the quantitative variable
    df = df.dropna(subset=[quantitative_variable])

    # Group by the categorical variable and calculate summary statistics
    grouped_stats = df.groupby(categorical_variable)[quantitative_variable].agg(['mean', 'median', 'min', 'max', 'std'])

    print(f"\nSummary statistics of {quantitative_variable} grouped by {categorical_variable}:")
    print(grouped_stats)
else:
    print(f"Error: Column names {categorical_variable} or {quantitative_variable} not found in the dataset.")