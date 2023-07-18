import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data into a DataFrame
data = pd.read_csv('Pokemon.csv')

# Feature Engineering
data['Attack-Defense'] = data['Attack'] - data['Defense']
data['SpAtk-SpDef'] = data['Sp. Atk'] - data['Sp. Def']

# Group data by Type 1 and Type 2, and calculate the average Total, Attack-Defense, and SpAtk-SpDef for each combination
grouped_data = data.groupby(['Type1', 'Type2']).agg({'Total': 'mean', 'Attack-Defense': 'mean', 'SpAtk-SpDef': 'mean'}).reset_index()

# Sort the data by average Total in descending order
sorted_data = grouped_data.sort_values('Total', ascending=False)

# Plotting - Average Total Power
plt.figure(figsize=(12, 6))
sns.barplot(data=sorted_data, x='Type1', y='Total', hue='Type2', palette='viridis')
plt.xlabel('Type 1')
plt.ylabel('Average Total')
plt.title('Average Total Power by Type Combination')
plt.xticks(rotation=90)
plt.legend(title='Type 2')
plt.show()

# Plotting - Attack-Defense Comparison
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Attack', y='Defense', hue='Type1', palette='rainbow')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Attack vs Defense by Type 1')
plt.legend(title='Type 1')
plt.show()

# Plotting - SpAtk-SpDef Comparison
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Sp. Atk', y='Sp. Def', hue='Type1', palette='rainbow')
plt.xlabel('Special Attack')
plt.ylabel('Special Defense')
plt.title('Special Attack vs Special Defense by Type 1')
plt.legend(title='Type 1')
plt.show()

# Statistical Analysis - Type Comparison
type_comparison = data[['Type1', 'Type2', 'Total']].copy()
type_comparison['Type Combination'] = type_comparison['Type1'] + ' - ' + type_comparison['Type2']

type_summary = type_comparison.groupby('Type Combination')['Total'].describe()

print(type_summary)
