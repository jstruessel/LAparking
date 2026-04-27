import pandas as pd
import ScatterPlotPlotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/jstruessel/LAparking/refs/heads/main/Los_Angeles_International_Airport__LAX__-_Parking_Lots_Current_Status_20250122.csv")
print(df.columns)
fig = px.scatter(df, x="TotalParkingSpaces", y="Occupied", color="FullCapacity", hover_data=["Long","Lat"])
fig.show()

fig2 = px.line(df, x="TotalParkingSpaces", y="Occupied", color="FullCapacity", hover_data=["Long","Lat"])
fig2.show()

