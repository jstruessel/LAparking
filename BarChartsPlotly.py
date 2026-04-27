import plotly.express as px
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/jstruessel/LAparking/refs/heads/main/Los_Angeles_International_Airport__LAX__-_Parking_Lots_Current_Status_20250122.csv")
print(df.columns)

fig = px.bar(df, x='LotDescription', y='Occupied', title='Occupied Spaces by Lot', color= "FullCapacity", hover_data=["Long","Lat"])
fig.show()