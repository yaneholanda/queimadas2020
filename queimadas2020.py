import streamlit as st
import pandas as pd
import numpy as np

st.title('Queimadas no Brasil em 2020')

DATE_COLUMN = 'data/hora'
df = pd.read_csv("Focos_2020-01-01_2020-12-31.csv")

st.subheader('Map of all pickups')
hist_values = np.histogram(df[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = df[df[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
