# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (make sure the CSV file is in the same folder)
df = pd.read_csv("USA_Housing.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Data transformation
# Create a new column (example: price per room)
df["Price_per_Room"] = df["Price"] / df["Avg. Area Number of Rooms"]

# Filter data (houses with price greater than 300000)
filtered_df = df[df["Price"] > 300000]

# Sort data by Price
sorted_df = df.sort_values(by="Price", ascending=False)

# Visualization 1: Line graph
plt.figure()
plt.plot(df["Avg. Area Income"], df["Price"])
plt.title("Income vs Price")
plt.xlabel("Average Area Income")
plt.ylabel("Price")
plt.show()

# Visualization 2: Bar chart (first 10 rows)
plt.figure()
plt.bar(range(10), df["Price"].head(10))
plt.title("Top 10 House Prices")
plt.xlabel("Index")
plt.ylabel("Price")
plt.show()

# Visualization 3: Histogram
plt.figure()
plt.hist(df["Price"], bins=20)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()