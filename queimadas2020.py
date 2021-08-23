import pandas as pd
import numpy as np

df = pd.read_csv("Focos_2020-01-01_2020-12-31.csv")
map_data = df

st.map(map_data)
