import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
file_path = r"Titanic.csv"
df = pd.read_csv(file_path)

# Display dataset preview
print("Dataset Preview:")
print(df.head())

# Set Seaborn style
sns.set_theme(style="whitegrid")

# Example 1: Survival distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Survived', palette='pastel', hue='Survived', legend=False)
plt.title('Survival Count')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.show()

# Example 2: Survival by gender
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Survived', hue='Sex', palette='muted')
plt.title('Survival by Gender')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.show()

# Example 3: Distribution of fare prices
plt.figure(figsize=(8, 5))
sns.histplot(df['Fare'], kde=True, bins=30, color='blue')
plt.title('Distribution of Fare Prices')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

# Example 4: Age distribution by survival status
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Survived', y='Age')
plt.title('Age Distribution by Survival')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Age')
plt.show()

# Example 5: Survival by passenger class
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Pclass', hue='Survived', palette='Set2')
plt.title('Survival by Passenger Class')
plt.xlabel('Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)')
plt.ylabel('Count')
plt.show()

# Example 6: Correlation heatmap of numerical variables
plt.figure(figsize=(10, 8))
sns.heatmap(df.select_dtypes(include=['float64', 'int64']).corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()