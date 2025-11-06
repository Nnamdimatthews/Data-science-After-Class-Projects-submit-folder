import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Score': [88, 92, 85, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display original data
print("Original Data:")
print(df)

# Manipulations
print("\nFiltered (Age > 25):")
print(df[df['Age'] > 25])

print("\nSorted by Score (descending):")
print(df.sort_values(by='Score', ascending=False))

print("\nAdd new column (Passed):")
df['Passed'] = df['Score'] >= 90
print(df)

print("\nAverage Score:")
print(df['Score'].mean())
