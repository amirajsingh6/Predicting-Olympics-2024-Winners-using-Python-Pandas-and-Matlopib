import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = r'C:\Users\amiraj\Downloads\Athletes.xlsx'
df = pd.read_excel(file_path)

# Count occurrences of each NOC
nocs_counts = df['NOC'].value_counts()

# Select top N NOCs to display (e.g., top 10)
top_n = 10
top_nocs = nocs_counts.head(top_n)
other_nocs_count = nocs_counts.iloc[top_n:].sum()

# Replace NOCs not in top N with 'Others'
df['NOC'] = df['NOC'].apply(lambda x: x if x in top_nocs else 'Others')

# Reorder the categories so that 'Others' appears last
df['NOC'] = pd.Categorical(df['NOC'], categories=list(top_nocs.index) + ['Others'], ordered=True)

# Plot count of athletes by NOC with detailed counts on bars
plt.figure(figsize=(12, 6))
ax = sns.countplot(x='NOC', data=df, palette='Set2')

# Add count values on top of each bar
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=11, color='black', xytext=(0, 5),
                textcoords='offset points')

plt.title(f'Top {top_n} National Olympic Committees (NOCs) with Others')
plt.xlabel('NOC')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
