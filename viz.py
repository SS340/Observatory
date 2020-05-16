
#%%
import databank as db
from databank import countryNames, codes
from data import data_snapshot,indicators_generic, fetch_collection, saved_collections, create_collection

#%%
from plotly import graph_objects as go
import plotly as plo 
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def graphSingular(type,x,y,title):
    fig = None
    if type == "Line":
        fig = go.Figure(
            data=[go.Scatter(x=x,y=y)],
            layout_title_text=title
            
        )

    if type == "Bar":
        fig = go.Figure(
            data=[go.Bar(y=y)],
            layout_title_text=title
        )
        
    if type == "Scatter":
        fig = go.Figure(
            data=[go.Scatter(x=x,y=y,mode='markers',)],
            layout_title_text=title
        )
    fig.update_layout(template="plotly_dark")
    return fig.show()

def multiscatter_quick(data,mode_,title,titles):
    fig = go.Figure(layout_title_text=title)
    X = []
    for series in data:
        X.append((len(series['period']),series['period'].tolist())) 
    x_= pd.Series(max(X)[1])
    for i,series in enumerate(data):
        fig.add_trace(go.Scatter(x=x_,y=series['value'],mode=mode_,name = titles[i]))
    fig.update_layout(template="plotly_dark")
    return fig.show()

def multigraph_series(data,x,title,modes,titles):
    fig = go.Figure(layout_title_text=title)
    X = []
    for series in data:
        X.append((len(series[x]),series[x].tolist())) 
    x_= pd.Series(max(X)[1])
    for i,series in enumerate(data):
        fig.add_trace(go.Scatter(x=x_,y=series['value'],mode=modes[i],name = titles[i]))
    fig.update_layout(template="plotly_dark")
    return fig.show()

def vizBN(G):
  from pyvis.network import Network
  Gviz = Network(notebook = True,height="500px", width="100%",font_color="white", bgcolor="#222222")
  Gviz.from_nx(G)
  Gviz.set_options("""var options = {
     "physics": {
      "barnesHut": {
        "gravitationalConstant": -9950,
        "centralGravity": 1.15,
        "springLength": 145,
        "springConstant": 0.055,
        "avoidOverlap": 0.2
      },
      "maxVelocity": 18,
      "minVelocity": 0.75
    },
  "nodes": {
      "color": {
        "border": "rgba(0,0,0,1)",
        "background": "rgba(229,218,171,1)",
        "highlight": {
          "border": "rgba(229,86,51,1)",
          "background": "rgba(255,207,70,1)"
        },
        "hover": {
          "border": "rgba(229,97,106,1)",
          "background": "rgba(255,206,118,1)"
        }
      },
      "font": {
        "face": "verdana"
      }
    },
    "edges": {
      "arrows": {
        "to": {
          "enabled": true,
          "scaleFactor": 0.4
        },
        "from": {
          "enabled": true,
          "scaleFactor": 0.4
        }
      },
      "color": {
        "color": "rgba(255,255,255,1)",
        "highlight": "rgba(255,67,61,1)",
        "hover": "rgba(255,36,47,1)",
        "inherit": "both"
      },
      "smooth": false
    }
  }"""
  )
  
  return Gviz.show("nx.html")
