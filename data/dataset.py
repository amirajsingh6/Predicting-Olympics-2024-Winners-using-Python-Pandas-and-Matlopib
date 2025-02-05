import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define the directory and file names
directory = "C:/Users/Ahmed/Downloads/archive/"
medals_file_path = os.path.join(directory, "Medals.xlsx")
gender_file_path = os.path.join(directory, "EntriesGender.xlsx")
teams_file_path = os.path.join(directory, "Teams.xlsx")

# Read the Excel files into DataFrames
medals_df = pd.read_excel(medals_file_path)
gender_df = pd.read_excel(gender_file_path)
teams_df = pd.read_excel(teams_file_path)

# Rename columns for consistency
medals_df.rename(columns={'Team/NOC': 'NOC'}, inplace=True)

# Calculate total medals for each country
medals_df['Total Medals'] = medals_df[['Gold', 'Silver', 'Bronze']].sum(axis=1)

# Sort and get the top 19 countries by total medals
top_19_countries = medals_df.nlargest(19, 'Total Medals')

# Calculate the percentage of total medals won by each top 19 country
total_medals = medals_df['Total Medals'].sum()
top_19_countries['Percentage'] = (top_19_countries['Total Medals'] / total_medals) * 100

# Calculate the probability of winning the 2024 Olympics based on 2021 data
top_19_countries['Probability (%)'] = (top_19_countries['Total Medals'] / total_medals) * 100

# Rank countries by total medals starting from 1
top_19_countries['Rank'] = top_19_countries['Total Medals'].rank(ascending=False, method='min').astype(int)

# Sort the DataFrame by rank
top_19_countries.sort_values('Rank', inplace=True)

# Compute the correlation matrix for the top 19 countries
correlation_matrix = top_19_countries[['Gold', 'Silver', 'Bronze', 'Total Medals', 'Percentage', 'Rank']].corr()

# Plot the scatter plot
plt.figure(figsize=(14, 8))
scatter = sns.scatterplot(x='Total Medals', y='Rank', size='Percentage', sizes=(100, 2000), data=top_19_countries, legend=False, palette='viridis')
scatter.invert_yaxis()  # Invert y-axis to have Rank 1 at the top
scatter.set_title('Top 19 Countries Winning Medals', fontsize=16)
scatter.set_xlabel('Total Medals', fontsize=14)
scatter.set_ylabel('Rank', fontsize=14)
scatter.grid(True)

# Annotate each point with the country name
for i, row in top_19_countries.iterrows():
    scatter.annotate(row['NOC'], (row['Total Medals'], row['Rank']), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()

# Plot the correlation heatmap
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, annot_kws={"size": 12})
heatmap.set_title('Correlation Matrix of Winning the Olympics', fontsize=16)
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=45, horizontalalignment='right')

plt.tight_layout()
plt.show()

# Create a new DataFrame for countries with their medals and probabilities
country_medals_df = top_19_countries[['NOC', 'Gold', 'Silver', 'Bronze', 'Total Medals', 'Percentage', 'Rank', 'Probability (%)']]

# Plot the heatmap for countries with their medals and probabilities with number formatting
plt.figure(figsize=(14, 8))
country_heatmap = sns.heatmap(country_medals_df.set_index('NOC').T, annot=True, cmap='viridis', cbar=False, fmt='.2f')
country_heatmap.set_title('Medal Counts and Probabilities for Top 19 Countries', fontsize=16)
country_heatmap.set_yticklabels(country_heatmap.get_yticklabels(), rotation=0)

plt.tight_layout()
plt.show()
