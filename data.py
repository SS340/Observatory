
import databank as db
from databank import countryNames, codes 
saved_collections = dict(generic=[('IMFWEO',['NGDP_RPCH','NGDPRPPPPCPCH','PPPGDP','PCPIPCH','BCA_NGDPD','GGXCNL_NGDP','LUR'],None,None),('IMFCPI',['PCPI_IX','PCPI_PC_CP_A_PT'],None,'Q'),('OECD',['NAEXKP03.GYSA','NAEXKP02.GYSA'],'MEI','Q')])
countries = [("China",['CHN',"CN"]),("India",['IND',"IN"]),("USA",['USA',"US"])]
def econdata_fetch(c_code,dset,indicators,s_dset,period):
    if dset == 'IMFCPI':
        db.imd_CPIdata(c_code[0],indicators)
    if dset == 'IMFWEO':
        db.imd_WEOdata(c_code[1],indicators,period)
    if dset == 'OECD':
        db.imd_CPIdata(c_code[0],indicators,s_dset,period)
    return

def create_collection(name,requests):
    global saved_collections 
    saved_collections[name] = requests
    return 

def collection(country,collection):
    global countryNames
    for request in collection:
        econdata_fetch(countryNames[country],**request)
    return

def fetch_collection(countries,saved_collection):
    for country in countries:
        collection(country,saved_collection)
    return

def indicators_generic(country,c_codes):
    global codes 
    db.add_country(codes,c_codes,country)
    db.imf_WEOdata(c_codes[0],['NGDP_RPCH','NGDPRPPPPCPCH','PPPGDP','PCPIPCH','BCA_NGDPD','GGXCNL_NGDP','LUR'])
    db.imf_CPIdata(c_codes[1],['PCPI_IX','PCPI_PC_CP_A_PT'],'A')
    db.OECD_data(c_codes[0],['NAEXKP03.GYSA','NAEXKP02.GYSA'],'MEI','A')
    return 

def update_generic():
    for country in countries:
        indicators_generic(*country)
    print("All generic indicators updated")
    return

def data_snapshot(country,indicators,start,end):
    snapshot = dict()
    global codes, countryNames
    for c in country:
        c_codes = countryNames[c]
        snapshot[c] = dict()
        for code in c_codes:
            for i in indicators:
                try:
                    frame = codes[code][i]
                    fr = frame.loc[(frame['period'] >= start)&(frame['period'] <= end)]
                    snapshot[c][i] = fr[['period','series_code','value','series_name']]
                except KeyError:
                    pass
    return snapshot
print("Data bank initialized. ")
print("")
# Fetches generic indicators and stores them by country  
# indicators_generic('India',['IND','IN'])

# Filters values by period, reduces the frame to date, value, code and name. 
# snapshot2 = data_snapshot(['India'],['PCPI_IX','NAEXKP02.GYSA'],'2012-01-01','2014-10-01')
# cpi = snapshot2['India']['PCPI_IX']
# gysa = snapshot2['India']['NAEXKP02.GYSA']
# print(cpi.head())

