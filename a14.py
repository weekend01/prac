import pandas as pd

# Load the dataset
file_path = r"C:\Users\ASUS\Desktop\DSML_practical\Covid Vaccine Statewise.csv"
df = pd.read_csv(file_path)

# A. Describe the dataset
print("Dataset Description:")
print(df.describe(include='all'))

# B. Number of males vaccinated
if 'Male(Individuals Vaccinated)' in df.columns:
    total_males_vaccinated = df['Male(Individuals Vaccinated)'].dropna().sum()
    print(f"\nTotal number of males vaccinated: {total_males_vaccinated}")
else:
    print("\nColumn 'Male(Individuals Vaccinated)' not found in the dataset.")

# C. Number of females vaccinated
if 'Female(Individuals Vaccinated)' in df.columns:
    total_females_vaccinated = df['Female(Individuals Vaccinated)'].dropna().sum()
    print(f"\nTotal number of females vaccinated: {total_females_vaccinated}")
else:
    print("\nColumn 'Female(Individuals Vaccinated)' not found in the dataset.")
