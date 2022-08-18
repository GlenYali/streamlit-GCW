import os
import requests
import leafmap.foliumap as leafmap
import streamlit as st
from requests.auth import HTTPBasicAuth

def app():

    st.title("Planet Imagery")
    
    PLANET_API_KEY = os.getenv("PL_API_KEY")
    
    BASE_URL = 'https://api.planet.com/basemaps/v1/mosaics'
    
    if PLANET_API_KEY is None:
    PLANET_API_KEY = '12345'
    #pass in your API key
    
    auth = HTTPBasicAuth(PLANET_API_KEY, '')
    # HTTPBasicAuth() wants a username & password; you can pass an empty string for the password
    
    res = requests.get(url=BASE_URL, auth=auth)
        print(res.status_code)
        # make a request to the Basemaps API and test the response
        
    
    #os.environ["PL_API_KEY"] = "12345"
    tile_format = "ipyleaflet"

    if os.environ.get("USE_FOLIUM") is not None:
        tile_format = "folium"
        # leafmap.planet_monthly()
        monthly_tiles = leafmap.planet_monthly_tiles(tile_format=tile_format)
        for tile in monthly_tiles:
            print(tile)

    m = leafmap.Map()
    m.add_planet_by_month(year=2022, month=7, api_key="PL_API_KEY")
    
    
