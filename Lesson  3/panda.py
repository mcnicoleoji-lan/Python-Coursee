# Import library
import pandas as pd

# Create sample data
data = {
    "Name": ["Sanjay", "Rahul", "Karan", "Wasim", "Ramesh"],
    "Marks": [35, 50, 20, 45, 25]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display data
print("Original Data:")
print(df)

# Add new column (Percentage)
df["Percentage"] = (df["Marks"] / 50) * 100

# Filter students who scored above 30
filtered_df = df[df["Marks"] > 30]

# Sort by Marks
sorted_df = df.sort_values(by="Marks", ascending=False)

# Show results
print("\nWith Percentage:")
print(df)

print("\nStudents with Marks > 30:")
print(filtered_df)

print("\nSorted Data:")
print(sorted_df)