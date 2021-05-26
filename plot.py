import pandas as pd

import plotly.express as px

df = pd.read_csv("https://s3-whitehatjrcontent.whjr.online/curriculum/PRO+Asset/Copy+of+data+-+data.csv")

fig = px.line(df, x="date", y="cases", color="country", title='Covid Cases')

fig.show()
