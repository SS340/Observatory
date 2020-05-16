from textcleaner import cleantext, cleantexts
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
#from syntax import syntax_list, syntax_score, syntax_s
import pandas as pd
from collections import Counter
#from db_tools import lowercaser
import numpy as np
import networkx as nx
def bn_probs(co_df, vocab, sents):
    prob_mat = []
    sentlist = [sent.split(" ") for sent in sents]
    vocab_flat = [item for sublist in sentlist for item in sublist]
    
    count = Counter(vocab_flat)

    sorted_count = dict(sorted(count.items()))
    
    freqs = list(sorted_count.values())
    for i, key in enumerate(vocab):
        row = co_df[key].tolist()
        probs = [e/freqs[i] for e in row] 
        prob_mat.append(probs)
    
    temp = np.array(prob_mat)
    temp = np.where(temp > 1.0, 1.0, temp)

    prob_df = pd.DataFrame(columns = vocab, index = vocab, data = temp)

    return prob_df

def return_cooc(docs):
    vec = CountVectorizer(ngram_range=(1,1))
    X = vec.fit_transform(docs)
    Xc = (X.T * X)
    Xc.setdiag(0)
    ccr = Xc.todense().tolist()
    vocab_d = vec.vocabulary_
    vocab = list(sorted(vocab_d.keys()))
    co_df = pd.DataFrame(columns = vocab, index = vocab, data = ccr)
    return co_df

def vocabulary(docs):
    vec = CountVectorizer(ngram_range=(1,1))
    X = vec.fit_transform(docs)
    vocab_d = vec.vocabulary_
    vocab = list(sorted(vocab_d.keys()))
    return vocab

def bn_table(bn,vocab):
    edges = []
    for w in vocab: 
        qry = bn[w]
        results = qry[qry > 0.01].index
        _results = qry[qry > 0.01]
        for i in results.tolist():
            edges.append((w,i,_results[i]))
    return edges 

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