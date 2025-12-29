
import streamlit as st
import ee
from google.oauth2 import service_account
import pandas as pd
import os
import plotly.express as px
from utils.gee_auth import auth_gee
from st_on_hover_tabs import on_hover_tabs
from page import home as home_page
from page import map as map_page  # Import fungsi dari pages

st.set_page_config(
    page_title="Aboveground Biomass Monitoring",
    page_icon="assets/icon.svg", 
    layout="wide")

if not auth_gee():
        st.error(" Google Earth Engine authentication failed!")
        st.stop()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&display=swap');
html, body, [data-testid="stAppViewContainer"], .main {
    min-height: 100vh;
    background: radial-gradient(circle, rgba(0, 0, 0, 1) 0%, rgba(66, 92, 37, 1) 100%, rgba(41, 77, 41, 1) 11%, rgba(0, 0, 0, 1) 100%);
    font-family: 'Space Grotesk', sans-serif !important;
}
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    font-family: 'Space Grotesk', sans-serif !important;
}
.main, .block-container {
    background: transparent !important;
}
</style>
""", unsafe_allow_html=True)



with st.sidebar:
    st.sidebar.image("assets/logo.svg", width=100)
    st.markdown("""
    <div style='text-align:center;'>
        <h3 style='color:#238b45; margin-bottom:0; margin-top:0.5rem;'>BIOMASS2025</h3>
        <p style='font-size:1.05rem; color:#A9A9A9; margin-top:0.2rem;'>
            Empowering Forest Conservation<br>with AI & Remote Sensing
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    tabs = on_hover_tabs(
            tab_names=['Home', 'Map'],
            icon_names=['home', 'map'],
        styles={
            'navtab': {
                'background-color': '#232323',
                'color': '#A9A9A9',
                'font-size': '22px',
                'font-family': "'Space Grotesk', sans-serif !important",
                'font-weight': 'bold',
                'transition': '.3s',
                'text-transform': 'uppercase',
                'letter-spacing': '0.04em',
                'display': 'flex',
                'gap': '24px',
                'justify-content': 'center',
            },
            'tabStyle': {
                'font-family': "'Space Grotesk', sans-serif !important",
                'list-style-type': 'none',
                'margin-bottom': '18px',
                'padding': '18px 40px',
                'background-color': '#232323',
                'color': '#A9A9A9',
                'transition': 'color 0.2s ease, box-shadow 0.2s',
                'border-radius': '16px',
                'box-shadow': '0 4px 16px rgba(0,0,0,0.15)',
                'display': 'flex',
                'align-items': 'center',
                'gap': '16px',
            },
            'tabStyle:hover': {
                'font-family': "'Space Grotesk', sans-serif !important",
                'color': '#ffd700',
                'cursor': 'pointer',
                'background-color': '#238b45',
                'box-shadow': '0 6px 24px rgba(35,139,69,0.25)',
            },
            'tabStyleActive': {
                'font-family': "'Space Grotesk', sans-serif !important",
                'color': '#ffffff',
                'background-color': '#238b45',
                'box-shadow': '0 6px 24px rgba(35,139,69,0.25)',
                'border-radius': '18px',
                'font-weight': 'bold',
                'font-size': '24px',
            },
            'iconStyle': {
                'position': 'static',
                'margin-right': '18px',
                'font-size': '32px',
            }
        },
        default_choice=0
    )
    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    if tabs == "Home":
        st.markdown("""
            <div style='background:rgba(35,139,69,0.10); border-radius:10px; padding:1em 1em 0.7em 1em; margin-bottom:1em;'>
                <b>Welcome to Biomass2025!</b><br>
                Discover how advanced AI and satellite data are revolutionizing forest monitoring in Cattien National Park. Dive into project insights and explore our mission for a greener future.
            </div>
        """, unsafe_allow_html=True)
    elif tabs == "Map":
        st.markdown("""
            <div style='background:rgba(35,139,69,0.10); border-radius:10px; padding:1em 1em 0.7em 1em; margin-bottom:1em;'>
                <b>Interactive Map Controls</b><br>
                Personalize your biomass visualization:<br>
                <ul style='margin-bottom:0;'>
                    <li><b>Color Palette</b> – Choose a color scheme for better data clarity</li>
                    <li><b>Year</b> – Select the year to view biomass estimates</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        palettes = {
            'Plasma': px.colors.sequential.Plasma,
            'Greens': ['f7fcf5', 'e5f5e0', 'c7e9c0', 'a1d99b', '74c476', '41ab5d', '238b45', '006d2c', '00441b'],
            'Viridis': px.colors.sequential.Viridis,
            'Earth': ['#f7f4f0', '#d4c5a9', '#a67c52', '#6b4423', '#3d2817']
        }
        selected_palette = st.selectbox("Color Palette", list(palettes.keys()), key="sidebar_palette")
        year_options = [2021, 2022, 2023, 2024]
        selected_year = st.selectbox("Year", year_options, index=0, key="sidebar_year")

# Konten utama
if tabs == "Home":
    home_page.show_home()
elif tabs == "Map":
    map_page.show_map(selected_year, selected_palette)
