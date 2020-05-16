import pandas as pd
from dbnomics import fetch_series, fetch_series_by_api_link 
import oec
params = dict(classification= 'hs92',trade_flow= None, year= None, origin= None, destination= None, product= None )
products = oec.get_products(params['classification'])
countryNames = dict()
codes = dict()
def set_values(tfl, yr, ctry, dest, prod):
    global params
    params["trade_flow"] = tfl
    params["year"] = yr
    params["origin"] = ctry
    params["destination"] = dest
    params["product"] = prod
    return params

def fetch_data(params):
    data = oec.get_trade(**params)
    return data

def add_country(codes,c_codes,name):
    global countryNames
    for code in c_codes:
        codes[code] = dict()
    print(" ")
    print('Country added: ' + name)
    countryNames[name] = c_codes
    return

def imf_WEOdata(code,indicators):
    global codes
    print('Fetching data '+str(indicators)+'...')
    for i in indicators:
        codes[code][i] = fetch_series('IMF'+'/'+'WEO'+'/'+code+"."+i) 
    print("Done") 
    return 

def imf_CPIdata(code,indicators,periods):
    global codes
    print('Fetching data '+str(indicators)+'...')
    for i in indicators:
        codes[code][i] = fetch_series('IMF'+'/'+'CPI'+'/'+periods+'.'+code+'.'+i)
    print("Done") 
    return

def OECD_data(code,indicators,dset,periods):
    global codes
    print('Fetching data '+str(indicators)+'...')
    for i in indicators:
        codes[code][i] = fetch_series('OECD'+'/'+dset+'/'+code+'.'+i+'.'+periods)
    print("Done")    
    return 


base_profile_description = 'NGDP_RPCH(GDP growth),NGDPRPPPPCPCH(GDP:PPP growth),PPPGDP(GDP:PPP),PCPIPCH(inflation),BCA_NGDPD(CA balance P-GDP),GGXCNL_NGDP(net lending/borrowing P-GDP),PCPI_IX(CPI),PCPI_PC_CP_A_PT(CPI growth),NAEXKP03.GYSA.Q(govexp),NAEXKP02.GYSA.Q(privexp)'
# add_country(codes,['IND','IN'],'India')
# imf_WEOdata('IND',['NGDP_RPCH','NGDPRPPPPCPCH','PPPGDP','PCPIPCH','BCA_NGDPD','GGXCNL_NGDP'])
# imf_CPIdata('IN',['PCPI_IX','PCPI_PC_CP_A_PT'],'Q')
# OECD_data('IND',['NAEXKP03.GYSA','NAEXKP02.GYSA'],'MEI','Q')


