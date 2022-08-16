import os
import leafmap
import leafmap.foliumap as leafmap
import streamlit as st

def app():

    st.title("Planet Imagery")

    os.environ["31848fad673b405f9c7eee934f1d2ad3"] = "12345"
    tile_format = "ipyleaflet"

    if os.environ.get("USE_FOLIUM") is not None:
        tile_format = "folium"
        # leafmap.planet_monthly()
        monthly_tiles = leafmap.planet_monthly_tiles(tile_format=tile_format)
        for tile in monthly_tiles:
            print(tile)

    m = leafmap.Map()
    m.add_planet_by_month(year=2022, month=7, api_key="31848fad673b405f9c7eee934f1d2ad3")
