#%%
from newsstream2 import headlines, summary
import textcleaner as tc 
import context as ct
c_headlines = tc.cleantexts(headlines)
cooc = ct.return_cooc(c_headlines)
bnprobs = ct.bn_probs(cooc,ct.vocabulary(cooc),cooc)
vocab = ct.vocabulary(cooc)
import networkx as nx
import matplotlib.pyplot as plt



#%%
def genBNgraph(bnprobs_,vocab_):
  edges = []
  for w in vocab_: 
      qry = bnprobs_[w]
      results = qry[qry > 0.01].index
      _results = qry[qry > 0.01]
      for i in results.tolist():
          edges.append((w,i,_results[i]))
  G = nx.DiGraph()
  for e in edges: 
      G.add_edge(e[0],e[1])
  return G

G2 = genBNgraph(bnprobs,vocab) 
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
vizBN(G2)
#%% 


# %%
