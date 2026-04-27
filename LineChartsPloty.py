import random
import pandas as pd
import ScatterPlotPlotly.express as px

random.seed(42)
# Generate 40 unique random numbers for 'x' between 1 and 40
y_unique_values = [random.randint(1, 10) for _ in range(40)]
# Generate 40 random numbers for 'y' between 1 and 10
x_unique_values = random.sample(range(1, 41), 40)
df_unique_x = pd.DataFrame({
    'y': y_unique_values,
    'x': x_unique_values
})

fig_unique_x = px.line(df_unique_x, x="x", y="y", title="Unsorted Input (df_unique_x)")
fig_unique_x.show()

df_unique_x_sorted = df_unique_x.sort_values(by="x")
fig_unique_x_sorted = px.line(df_unique_x_sorted, x="x", y="y", title="Sorted Input (df_unique_x)")
fig_unique_x_sorted.show()