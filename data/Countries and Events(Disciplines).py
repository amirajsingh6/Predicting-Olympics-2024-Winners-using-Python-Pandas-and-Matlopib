import pandas as pd
 import matplotlib.pyplot as plt
 import seaborn as sns

 file_path = r'C:\Users\amiraj\Downloads\Teams.xlsx'


 team_discipline_counts = df.groupby(['Discipline', 'Name']).size().reset_index(name='Count')


 team_discipline_pivot = team_discipline_counts.pivot(index='Discipline', columns='Name', values='Count').fillna(0)
 country_counts = team_discipline_pivot.sum(axis=0)
 top_10_countries = country_counts.nlargest(10).index
 team_discipline_pivot_top10 = team_discipline_pivot[top_10_countries]
 plt.figure(figsize=(12, 8))
 heatmap = sns.heatmap(team_discipline_pivot_top10, annot=True, fmt='.0f', cmap='YlGnBu', linewidths=.5)

 plt.title('Count of Teams by Discipline (Top 10 Countries)')
 plt.xlabel('Countries')  # Adjusted xlabel here
 plt.ylabel('Discipline')
 plt.xticks(rotation=90)
 plt.yticks(rotation=0)
 plt.tight_layout()
 plt.show()
