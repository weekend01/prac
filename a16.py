import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\ASUS\Desktop\DSML_practical\Titanic.csv"
df = pd.read_csv(file_path)

# Check if 'fare' column exists
if 'Fare' in df.columns:
    # Plot the histogram of 'fare'
    plt.figure(figsize=(10, 6))
    plt.hist(df['Fare'].dropna(), bins=30, color='skyblue', edgecolor='black')
    plt.title('Distribution of Ticket Fare on Titanic', fontsize=16)
    plt.xlabel('Fare', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(axis='y', alpha=0.75)
# Adds horizontal grid lines to the plot for better readability.
# axis='y' ensures the grid lines are only on the y-axis.
# alpha=0.75 controls the transparency of the grid lines.

    plt.show()
else:
    print("'fare' column not found in the dataset.")

# df['fare'].dropna():
# Drops any rows where the fare value is missing (i.e., NaN) to ensure only valid values are plotted.
# bins=30:
# Divides the range of fare values into 30 intervals (bins) for the histogram.
# color='skyblue':
# Fills the bars of the histogram with a light blue color.
# edgecolor='black':
# Adds black outlines to the edges of the histogram bars for better visibility.