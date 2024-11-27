import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\ASUS\Desktop\DSML_practical\IRIS.csv"  # Update with your correct file path
df = pd.read_csv(file_path)

# Display the dataset
print("Dataset Head:")
print(df.head())

# 1. Create box plots for each feature
print("\nCreating box plots for each feature...")
for column in df.columns[:-1]:  # Exclude the target column (e.g., Species)
    plt.figure(figsize=(8, 6))
    plt.boxplot(df[column], patch_artist=True, notch=True, boxprops=dict(facecolor='skyblue', color='black'))
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.ylabel('Values')
    plt.grid(axis='y')
    plt.show()  # Show each plot before continuing

# 2. Identify outliers
print("\nOutlier Analysis:")
for column in df.columns[:-1]:  # Exclude the target column
    Q1 = df[column].quantile(0.25)  # First quartile
    Q3 = df[column].quantile(0.75)  # Third quartile
    IQR = Q3 - Q1  # Interquartile range
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"\nOutliers for {column}:")
    print(f" - Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
    print(f" - Number of Outliers: {len(outliers)}")
    if len(outliers) > 0:
        print(f" - Outlier Values:\n{outliers[column].values}")
    else:
        print(f" - No outliers detected.")
