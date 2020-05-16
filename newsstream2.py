# news API key:6733309a4f9342bb943ea87fb30e1b6c
# TODO generate rich text files with the called data
from classes import req_e, req_h
from newsapi import NewsApiClient
import ijson, json
import pandas as pd
import csv
import numpy as np
import datetime as dt

news = NewsApiClient(api_key='6733309a4f9342bb943ea87fb30e1b6c')
report = str
articles = None
headlines = None
summary = None
frm = None
today = str(dt.datetime.now().date())

def get_trainingdata_TEST(req_h):
    global report
    #news.get_everything(q= frm, sources= req_h.sources, language= req_h.language, to = req_h.to, sort_by= req_h.sortBy, page_size= req_h.pageSize)
    report = news.get_top_headlines(q= frm, sources= req_h.sources, language= req_h.language, page_size= req_h.pageSize)
    return report

def generatestream(report):
    with open('nstream.json', 'w') as stream:
        return json.dump(report, stream)

def getcontent():
    global articles
    global headlines
    global summary
    with open('nstream.json', 'r') as stream:
        articlestream = ijson.items(stream, 'articles')
        k = list(articlestream)
        articles = list(k[0])
        headlines = [title['title'] for title in articles ]
        summary = [sum['description'] for sum in articles]
        sources = list(set([s["source"]["name"] for s in articles]))
        print('successfully fetched articles')
        print("Total articles", len(headlines))
        print("Sources: ", sources)
        return headlines, summary

def newsstream(req_h):
    # testdeploy(req_h)
    get_trainingdata_TEST(req_h)
    generatestream(report)
    getcontent()
    return 

newsstream(req_h(q = None, sources = 'reuters,bbc-news, associated-press,google-news,bloomberg', category = 'World', language = 'en', country = None, pageSize = 100))

# ,bbc-news, associated-press,google-news,bloomberg
# newsstream(req_h(q = None, sources = 'reuters', category = None,
#                 language = 'en', country = None, to = today, sortBy = 'relevancy',
#                 pageSize = 100))
