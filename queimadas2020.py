import pandas as pd
import numpy as np
import streamlit as st

from streamlit_folium import folium_static
import folium

"# streamlit-folium"
df = pd.read_csv("Focos_2020-01-01_2020-12-31.csv", sep = ",")

df.columns

#lat = pd.to_numeric(df["latitude"], errors='coerce')
#lon = pd.to_numeric(df["longitude"], errors='coerce')
lat = df['latitude']
long = df['longitude']

with st.echo():
    import streamlit as st
    from streamlit_folium import folium_static
    import folium

    # center on Liberty Bell
    m = folium.Map(location= (lat, lon), zoom_start=16)

    # add marker for Liberty Bell
    #tooltip = "Liberty Bell"
    #folium.Marker(
    #    [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
    #).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)
