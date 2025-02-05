import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = r'C:\Users\amiraj\Downloads\Teams.xlsx'
df = pd.read_excel(file_path)


print(df.head())
print(df.columns)


print(df.dtypes)
print(df.isnull().sum())
teams_by_discipline = df['Discipline'].value_counts()
teams_by_event = df['Event'].value_counts()
plt.figure(figsize=(12, 6))
sns.countplot(x='Discipline', data=df, palette='Set2', order=teams_by_discipline.index)
plt.title('Count of Teams by Discipline')
plt.xlabel('Discipline')
plt.ylabel('Count')
plt.xticks(rotation=45)


for index, value in enumerate(teams_by_discipline):
	plt.text(index, value + 0.5, str(value), ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
sns.countplot(x='Event', data=df, palette='Set3', order=teams_by_event.index)
plt.title('Count of Teams by Event')
plt.xlabel('Event')
plt.ylabel('Count')
plt.xticks(rotation=45)


for index, value in enumerate(teams_by_event):
	plt.text(index, value + 0.5, str(value), ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()
