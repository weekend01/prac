import pandas as pd

# Load the dataset
file_path = r"C:\Users\ASUS\Desktop\DSML_practical\IRIS.csv"
df = pd.read_csv(file_path)

# Filter the dataset for each species
species_list = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# Iterate through each species and display statistical details
for species in species_list:
    print(f"Statistics for {species}:")
    species_data = df[df['species'] == species]  # Filter data for the species
    print(species_data.describe())  # Display statistical details
    print("\n")




# Filter the rows:

# df[...] is used to filter rows where the condition inside the brackets evaluates to True.
# Only rows where df['species'] == species is True are included in the resulting species_data.
# Example for species = 'Iris-setosa':

# The filtered DataFrame (species_data) contains only rows where the species is "Iris-setosa", i.e., the first 50 rows.