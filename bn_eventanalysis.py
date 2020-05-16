from itertools import islice
from collections import Counter
import collections
import networkx.algorithms as xa
import networkx as nx
import collections
import context as ct

def list_diff(list1, list2):
    list1_ = [k[1] for k in list1]
    list2_ = [k[1] for k in list2]
    return len((Counter(list1_) - Counter(list2_)).values())

def detect_N(n,graph):
    def take(n, iterable):
        return list(islice(iterable, n))
    cent = sorted(xa.in_degree_centrality(graph).items(), key=lambda kv: kv[1])[::-1]
    centrality = collections.OrderedDict(cent)
    entities = take(20,centrality.items())
    return dict(entities) 


def clones(graph,entities):
    G = []
    for e1 in list(entities.keys()):
        g = []
        for e2 in list(entities.keys()):
            if e2 == e1:
                pass
            elif list_diff(list(graph.edges(e1)),list(graph.edges(e2))) <= 1:
                g.append(e2)
        G.append((e1,g))
    res = dict(G)
    return res


def resolve(entities,res):
    deleted = []
    for e in list(res.keys()):
        if res[e] == []:
            pass
        else:
            for i in res[e]:
                try:
                    if entities[e] > entities[i]:
                        entities.pop(i)
                        deleted.append(i)
                except KeyError:
                        pass
                try:
                    if entities[e] < entities[i]:
                        entities.pop(e)
                except KeyError:
                        pass
                try:
                    if entities[e] == entities[i]:
                        entities.pop(i)
                except KeyError:
                        pass    
    return entities


def n_events(n,graph,entities):
    cent = sorted(xa.in_degree_centrality(graph).items(), key=lambda kv: kv[1])[::-1]
    centrality = collections.OrderedDict(cent)
    def take(n, iterable):
        return list(islice(iterable, n))

    events = []
    for i in entities.keys():
        n = [k[1] for k in list(graph.edges(i))]
        vals = []
        for f in n:
            vals.append((f,centrality[f]))
        events.append([i]+take(10,dict(vals)))
    return events 


