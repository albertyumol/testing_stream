
"""
A streamlit app to draw a Mohr's Circle based on user input
using the Bokeh plotting library
"""

import numpy as np
import streamlit as st
from bokeh.plotting import figure
import pandas as pd


st.title("Customer Segmentation Project")

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
countries = pd.read_csv('https://eskwelabs-ds5.s3-ap-southeast-1.amazonaws.com/countries_1.csv')
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.sidebar.markdown('test')

countries = countries[:10]

from bokeh.models import ColumnDataSource
from bokeh.palettes import Category20c

country = list(countries['country'])
count = list(countries['count'].astype(int))

source = ColumnDataSource(data=dict(country=country, count=count, color=Category20c[len(country)]))

p = figure(x_range=country, plot_height=500, plot_width=800, y_range=(0, 360000), title="Country Counts")
p.vbar(x='country', top='count', width=0.5, color='color', legend_field="country", source=source)

p.xgrid.grid_line_color = None

st.bokeh_chart(p)

# st.title("Mohr's Circle App")
#
# stress_x = st.sidebar.number_input("stress in x", value=2.0, step=0.1)
# stress_y = st.sidebar.number_input("stress in y", value=5.0, step=0.1)
# shear = st.sidebar.number_input("shear xy", value=4.0, step=0.1)
#
# # find center and radius
# C, R = mohr_c(stress_x, stress_y, shear)
#
# # build arrays plot circle
# circle_x, circle_y = c_array(C, R)
#
# # build arrays to plot line through the circle
# X, Y = X_Y(stress_x, stress_y, shear)
#
# st.sidebar.markdown(f"max stress = {round(C+R,2)}")
# st.sidebar.markdown(f"min stress = {round(C-R,2)}")
# st.sidebar.markdown(f"max shear = {round(R,2)}")
#
# p = figure(
#     title="Mohr's Circle",
#     x_axis_label="stress",
#     y_axis_label="shear",
#     match_aspect=True,
#     tools="pan,reset,save,wheel_zoom",
# )
#
# p.line(circle_x, circle_y, color="#1f77b4", line_width=3, line_alpha=0.6)
# p.line(X, Y, color="#ff7f0e", line_width=3, line_alpha=0.6)
#
# p.xaxis.fixed_location = 0
# p.yaxis.fixed_location = 0
#
# st.bokeh_chart(p)
