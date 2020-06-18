#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:09:48 2020

@author: ubuntu
"""


import seaborn as sns
import pandas as pd
import folium
from folium import plugins
import webbrowser

df = pd.read_csv('AnalyticEnv/MapData/kc_house_data.csv', parse_dates=['date'])
print(df.head())

print(df[['lat','long']])

m = folium.Map([df['lat'].mean(),df['long'].mean()],zoom_start=12)

fm = folium.Marker(location = [df['lat'].mean(), df['long'].mean()],
                  popup = 'Centre Point',
                  icon = folium.Icon(color='red', icon  ='info-sign'))
fm.add_to(m)

mc = plugins.MarkerCluster().add_to(m)

counter = 10
for idx, data in df.iterrows():
    if idx < counter:
        folium.Marker(location = [data['lat'], data['long']],
                  popup = 'size - {}'.format(data['sqft_above'])).add_to(mc)
    else:
        break

m.save('map.html')
webbrowser.open_new_tab('map.html')

