import pandas as pd

import plotly.express as px

#reading data from csv files
df = pd.read_csv("https://s3-whitehatjrcontent.whjr.online/curriculum/PRO+Asset/Copy+of+data+-+data.csv")
fig = px.bar(df, x='date', y='cases', color="country")
fig.show()
