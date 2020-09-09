
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
df = pd.read_csv('https://eskwelabs-ds5.s3-ap-southeast-1.amazonaws.com/E_cluster_validation_data.txt', sep=",", header=None)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')



countries = countries[:10]

from bokeh.models import ColumnDataSource
from bokeh.palettes import Category20c
from bokeh.palettes import Spectral6

country = list(countries['country'])
count = list(countries['count'].astype(int))

source1 = ColumnDataSource(data=dict(country=country, count=count, color=Category20c[len(country)]))

p = figure(x_range=country, plot_height=500, plot_width=800, y_range=(0, 360000), title="Country Counts")
p.vbar(x='country', top='count', width=0.5, color='color', legend_field="country", source=source1)

p.xgrid.grid_line_color = None

st.bokeh_chart(p)





from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# normalize data
X = df.values
sc = StandardScaler()
sc.fit(X)
X = sc.transform(X)

st.sidebar.markdown('Number of Clusters')
n_clusters = st.sidebar.number_input("k = ", value=2, step=1)


clusterer = KMeans(n_clusters=n_clusters,max_iter=1000, random_state=10)
cluster_labels = clusterer.fit_predict(X)

spectral = np.hstack([Spectral6] * 20)
colors = [spectral[i] for i in cluster_labels]
#     #colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
plot = figure(plot_height=500, plot_width=800, title='Clusters')
source = ColumnDataSource(data=dict(x=X[:, 0], y=X[:, 1], colors=colors))
plot.scatter('x', 'y', fill_color='colors', line_color=None, source=source)
st.bokeh_chart(plot)
