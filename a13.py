import pandas as pd

# Load the dataset
file_path = r"C:\Users\ASUS\Desktop\DSML_practical\Covid Vaccine Statewise.csv"
df = pd.read_csv(file_path)

# a. Describe the dataset
print("Dataset Description:")
print(df.describe(include='all'))
print("\nDataset Info:")
print(df.info())

# b. Number of persons state-wise vaccinated for the first dose
if 'State' in df.columns and 'First Dose Administered' in df.columns:
    first_dose_statewise = df.groupby('State')['First Dose Administered'].sum()
    print("\nNumber of persons state-wise vaccinated for the first dose:")
    print(first_dose_statewise)
else:
    print("\nColumns 'State' or 'First Dose Administered' not found in the dataset.")

# c. Number of persons state-wise vaccinated for the second dose
if 'State' in df.columns and 'Second Dose Administered' in df.columns:
    second_dose_statewise = df.groupby('State')['Second Dose Administered'].sum()
    print("\nNumber of persons state-wise vaccinated for the second dose:")
    print(second_dose_statewise)
else:
    print("\nColumns 'State' or 'Second Dose Administered' not found in the dataset.")
