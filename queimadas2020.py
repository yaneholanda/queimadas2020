import streamlit as st
import numpy as np
import pandas as pd


st.title('Queimadas no Brasil em 2020')

df = pd.read_csv("Focos_2020-01-01_2020-12-31.csv")
df = df.sample(frac=1).reset_index(drop=True)
  
  
st.subheader('Map of all pickups')
st.map(df)
