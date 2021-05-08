#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from bokeh.plotting import figure, output_file, show
import pandas as pd
import os
from pathlib import Path
"""Define Path for Home directory"""
HOME_DIR = str(Path.home())
"""Reading the downloaded data"""
GEData = pd.read_csv(os.path.join(HOME_DIR, 'Desktop', 'projects', 'TestandFeatures', 'weather', 'data', 'GE.csv'))
BoeingData = pd.read_csv(os.path.join(HOME_DIR, 'Desktop', 'projects', 'TestandFeatures', 'weather', 'data', 'BA.csv'))
AirbusData = pd.read_csv(os.path.join(HOME_DIR, 'Desktop', 'projects', 'TestandFeatures', 'weather', 'data', 'AIR.PA.csv'))
SafranData = pd.read_csv(os.path.join(HOME_DIR, 'Desktop', 'projects', 'TestandFeatures', 'weather', 'data', 'SAF.PA.csv'))
"""The function creates an array for the input list"""
def datetime(x):
    return np.array(x, dtype=np.datetime64)
"""Defining the Parameters for the figure"""
p1 = figure(x_axis_type="datetime", title="Stock Open Prices")
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date: May 2020 to May 2021'
p1.yaxis.axis_label = 'Open Price'

p1.line(datetime(GEData['Date']), GEData['Open'], color='black', legend_label='GE')
p1.circle(datetime(GEData['Date']), GEData['Open'], color='black', legend_label='GE')
p1.line(datetime(BoeingData['Date']), BoeingData['Open'], color='red', legend_label='Boeing')
p1.triangle(datetime(BoeingData['Date']), BoeingData['Open'], color='red', legend_label='Boeing')
p1.line(datetime(AirbusData['Date']), AirbusData['Open'], color='blue', legend_label='Airbus')
p1.triangle(datetime(AirbusData['Date']), AirbusData['Open'], color='blue', legend_label='Airbus')
p1.line(datetime(SafranData['Date']), SafranData['Open'], color='green', legend_label='Safran')
p1.circle(datetime(SafranData['Date']), SafranData['Open'], color='green', legend_label='Safran')
p1.legend.location = "top_left"
"""Defining the output file"""
output_file("logplot.html", title="Comparison of 'Open' Stock Share Prices for the past one year")
show(p1)
