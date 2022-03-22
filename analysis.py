import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
mean_of_data = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

figure = px.scatter(mean_of_data, x="student_id",
y="level",size="attempt", color="attempt", orientation="h")

figure.show()