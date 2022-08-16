import os
import requests
import leafmap
import leafmap.foliumap as leafmap
import streamlit as st

def app():

    st.title("Planet Imagery")

    from requests.auth import HTTPBasicAuth
# import helper functions to make Basic request to Planet API

    PLANET_API_KEY = os.getenv("31848fad673b405f9c7eee934f1d2ad3")
# Setup the API Key from the `PL_API_KEY` environment variable

    BASE_URL = 'https://api.planet.com/basemaps/v1/mosaics'

    if PLANET_API_KEY is None:
       PLANET_API_KEY = '12345'
#pass in your API key

    auth = HTTPBasicAuth(PLANET_API_KEY, '')
# HTTPBasicAuth() wants a username & password; you can pass an empty string for the password

    res = requests.get(url=BASE_URL, auth=auth)

      print(res.status_code)
# make a request to the Basemaps API and test the response

    
