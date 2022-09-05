import os
import leafmap.foliumap as leafmap
import streamlit as st
import requests

def app():

    st.title("Planet Imagery")
    
    st.write(
    "Has environment variables been set:",
    os.environ["PLANET_API_KEY"] == st.secrets["PLANET_API_KEY"],
)  

    BASE_URL = 'https://api.planet.com/basemaps/v1/mosaics'
    res = requests.get(url=BASE_URL)

    
    os.environ["PLANET_API_KEY"] = "12345"
    tile_format = "ipyleaflet"
    
    if os.environ.get("USE_FOLIUM") is not None:
        tile_format = "folium"
        # leafmap.planet_monthly()
        monthly_tiles = leafmap.planet_monthly_tiles(tile_format=tile_format)
        for tile in monthly_tiles:
            print(tile)

    m = leafmap.Map()
    m.add_planet_by_month(year=2022, month=7, api_key="PLANET_API_KEY")
    
   







    
