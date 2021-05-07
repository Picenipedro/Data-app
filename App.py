App.py
import pandas as pd
import plotly.express as px

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server

#---------------------------------------------

excel = pd.read_csv(r'C:\Users\Peter\Data explotation web - App\Data')

excel.head()




