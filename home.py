## Home editor ##
## Run cell to start program: ## 
# %%
## Welcome to the observatory ##
import databank as db
from databank import countryNames,codes
from viz import graphSingular,multiscatter_quick,vizBN
from data import countries, saved_collections
import data
#######################################################DO NOT EDIT ABOVE###############################################
# Start below here
#%%
data.update_generic()
# EXAMPLE WORKFLOW: fetch data --> data_snapshot --> define series --> charting and analysis 
# data_generic = data.data_snapshot(['USA','China','India'],['NGDP_RPCH','LUR','PCPI_PC_CP_A_PT',],'2016-01-01','2020-10-01')
# unemployment_USA = data_generic['USA']['LUR']
# us_GDPgrowth = data_generic['USA']['NGDP_RPCH']
# us_govexp = data_generic['USA']['PCPI_PC_CP_A_PT']
# multiscatter_quick([us_GDPgrowth,unemployment_USA,us_govexp],'lines+markers','Country overview: USA',['GDP growth','Unemployment','CPI'])

# %%
from newsstream2 import headlines, summary
import textcleaner as tc 
import context as ct
c_headlines = tc.cleantexts(headlines)
cooc = ct.return_cooc(c_headlines)
bnprobs = ct.bn_probs(cooc,ct.vocabulary(cooc),cooc)
vocab = ct.vocabulary(cooc)
bn_graph = ct.genBNgraph(bnprobs,vocab)
vizBN(bn_graph)

 

# %%
 



# %%
