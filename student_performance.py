import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')
student_df = df.loc[df['student_id']=='TRL_987']
mean_df = df.groupby(['student_id', 'level'], as_index = False)['attempt'].mean()
print(mean_df)
fig = px.scatter(
    mean_df,
    x = 'student_id', 
    y = 'level',
    color = 'attempt',
    size = 'attempt'
)
fig.show()