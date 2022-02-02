
import time,threading
import requests,json
import queue, pandas as pd
import numpy as np





#sc-chbBtj eFnQzh
def get_perf1(id):
        
    link=f'https://www.winamax.fr/paris-sportifs/match/{id}'
    #print(link)
    res = requests.get(link, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"})
    html = res.text
    first = html.split("var PRELOADED_STATE = ")[1]
    last = first.split(";</script>")[0]
    matche=json.loads(last)
        
    try:
        div1 = matche['bets']
        titre = matche['matches'][id]["title"]
        
        names=[]
        data1=[]
        data2=[]
        data3=[]
        data4=[]
        data5=[]
        data6=[]
        for item in div1:
            if "Total du joueur (points + rebonds + passes)" in div1[item]['betTypeName']:
                
                name = div1[item]['betTypeName'].split(" - ")[1]
                
                points = (div1[item]['specialBetValue'].split('|total=')[1])
                temp =[n["name"] for n in names]
                if name not in temp:
                    names.append({"name":name})
                #print(name,points)
                data1.append({'name':name,'Total du joueur (points + rebonds + passes) WINAMAX':points})
            elif "Total du joueur (points + passes)" in div1[item]['betTypeName']:
                name = div1[item]['betTypeName'].split(" - ")[1]
                points = (div1[item]['specialBetValue'].split('|total=')[1])
                temp =[n["name"] for n in names]
                if name not in temp:
                    names.append({"name":name})
                #print(name,points)
                data2.append({'name':name,'Total du joueur (points + passes) WINAMAX':points})
            elif "Total du joueur (points + rebonds)" in div1[item]['betTypeName']:
                name = div1[item]['betTypeName'].split(" - ")[1]
                points = (div1[item]['specialBetValue'].split('|total=')[1])
                temp =[n["name"] for n in names]
                if name not in temp:
                    names.append({"name":name})
                #print(name,points)
                data3.append({'name':name,'Total du joueur (points + rebonds) WINAMAX':points})
            elif "Total du joueur (passes + rebonds)" in div1[item]['betTypeName']:
                name = div1[item]['betTypeName'].split(" - ")[1]
                points = (div1[item]['specialBetValue'].split('|total=')[1])
                temp =[n["name"] for n in names]
                if name not in temp:
                    names.append({"name":name})
                #print(name,points)
                data4.append({'name':name,'Total du joueur (passes + rebonds) WINAMAX':points})
            elif "Nombre de passes décisives du joueur" in div1[item]['betTypeName']:
                name = div1[item]['betTypeName'].split(" - ")[1]
                points = (div1[item]['specialBetValue'].split('|total=')[1])
                temp =[n["name"] for n in names]
                if name not in temp:
                    names.append({"name":name})
                #print(name,points)
                data5.append({'name':name,'Nombre de passes décisives du joueur WINAMAX':points})
            elif "Nombre de rebonds du joueur" in div1[item]['betTypeName']:
                name = div1[item]['betTypeName'].split(" - ")[1]
                points = (div1[item]['specialBetValue'].split('|total=')[1])
                temp =[n["name"] for n in names]
                if name not in temp:
                    names.append({"name":name})
                #print(name,points)
                data6.append({'name':name,'Nombre de rebonds du joueur WINAMAX':points})
            #Nombre de rebonds du joueur
            
        for item in names:
            item['titre']=titre
            index =[i for i in range(len(data1)) if data1[i]["name"]==item["name"]]
            
            if index != []:
                item['Total du joueur (points + rebonds + passes) WINAMAX']=data1[index[0]]['Total du joueur (points + rebonds + passes) WINAMAX']
            index1 =[i for i in range(len(data2)) if data2[i]["name"]==item["name"]]
            if index1 != []:
                item['Total du joueur (points + passes) WINAMAX']=data2[index1[0]]['Total du joueur (points + passes) WINAMAX']
            index2 =[i for i in range(len(data3)) if data3[i]["name"]==item["name"]]
            if index2 != []:
                item['Total du joueur (points + rebonds) WINAMAX']=data3[index2[0]]['Total du joueur (points + rebonds) WINAMAX']
            index3 =[i for i in range(len(data4)) if data4[i]["name"]==item["name"]]
            if index3 != []:
                item['Total du joueur (passes + rebonds) WINAMAX']=data4[index3[0]]['Total du joueur (passes + rebonds) WINAMAX']
            index4 =[i for i in range(len(data5)) if data5[i]["name"]==item["name"]]
            if index4 != []:
                item['Nombre de passes décisives du joueur WINAMAX']=data5[index4[0]]['Nombre de passes décisives du joueur WINAMAX']
            index5 =[i for i in range(len(data6)) if data6[i]["name"]==item["name"]]
            if index5 != []:
                item['Nombre de rebonds du joueur WINAMAX']=data6[index5[0]]['Nombre de rebonds du joueur WINAMAX']
        
        df2 = pd.DataFrame(names)
        
        return(df2)
    
    except Exception as e:
        print(e)
        pass

#sc-iiSMjD bjpXrA
def get_matches():
    res = requests.get('https://www.winamax.fr/paris-sportifs/sports/2/15/177', headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"})
    html = res.text
    first = html.split("var PRELOADED_STATE = ")[1]
    last = first.split(";</script>")[0]
    matches=json.loads(last)['matches']
    data = pd.DataFrame(columns=['titre', 'name', 'Total du joueur (points + rebonds + passes) WINAMAX','Total du joueur (points + passes) WINAMAX',"Total du joueur (points + rebonds) WINAMAX","Total du joueur (passes + rebonds) WINAMAX","Nombre de passes décisives du joueur WINAMAX","Nombre de rebonds du joueur WINAMAX"])

    for match in matches:
            if matches[match]['sportId']==2:
                id= (matches[match]['matchId'])
                #print(id)
                try : 
                    
                    rec= (get_perf1(str(id)))
                    time.sleep(1)
                    if len(rec):
                        data=data.append(rec,ignore_index=True)
                    
                except Exception as e:
                    print(e)
                    time.sleep(1)
                    continue
                
    #with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            #print(data)
    
    return data



#https://m.betclic.com/en/sports-betting/basketball-s4/nba-c13
def betclic_m():
    
        res = requests.get('https://offer.cdn.betclic.fr/api/pub/v2/competitions/13?application=2&countrycode=ma&fetchMultipleDefaultMarkets=true&forceCompetitionInfo=true&language=fr&sitecode=frfr')
        data = pd.DataFrame(columns=['name', 'Total du joueur (points + rebonds + passes) BETCLIC','Total du joueur (points + passes) BETCLIC',"Nombre total de points + rebonds BETCLIC","Nombre total de passes + rebonds BETCLIC","Nombre de passes décisives du joueur BETCLIC","Nombre total de rebonds du joueur BETCLIC"])
        res =json.loads( res.content)
        i=0
        for link in res['unifiedEvents']:
            try : 
                #print(link['id'])
                rec= (betclic_per(link['id']))
                time.sleep(1)
                if len(rec):
                    data=data.append(rec,ignore_index=True)
                
            except Exception as e:
                print(e)
                time.sleep(1)
                continue
        
        queue1.put(data)
    
def betclic_per(code):
    #https://offer.cdn.betclic.fr/api/pub/v5/events/3000923835?application=2&countrycode=ma&language=fr&sitecode=frfr
    try:
        res = requests.get(f'https://offer.cdn.betclic.fr/api/pub/v5/events/{code}?application=2&countrycode=ma&language=fr&sitecode=frfr')
        title= json.loads( res.content)['contestants'][0]['name']
        data1 = []
        
        perf1 = [perf for perf in json.loads( res.content)['grouped_markets'] if perf["name"]=="Performance du joueur (pts+reb+passes)" or perf["name"]=="Performance du joueur (points + rebonds + passes)" ]
        
        perf2 = [nbp for nbp in json.loads( res.content)['grouped_markets'] if nbp["name"]=="Nombre total de points + passes"]
        #
        
        perf3 = [nbp for nbp in json.loads( res.content)['grouped_markets'] if nbp["name"]=="Nombre total de points + rebonds"]
        
        perf4 = [nbp for nbp in json.loads( res.content)['grouped_markets'] if nbp["name"]=="Nombre total de passes + rebonds"]
        
        perf5 = [nbp for nbp in json.loads( res.content)['grouped_markets'] if nbp["name"]=="Nombre de passes décisives du joueur" or nbp["name"]=="Nombre total de passes du joueur"]
        
        perf6 = [nbp for nbp in json.loads( res.content)['grouped_markets'] if nbp["name"]=="Nombre total de rebonds du joueur"]
        
        names=[]
        if perf1 != []:
            perf1=perf1[0]
            for item in perf1['markets'][0]['selections']:
                #,'Total du joueur (points + rebonds + passes) BETCLIC':item[0]['name'].split('+ ')[-1].split('de ')[-1],"Total du joueur (points + passes) BETCLIC":"","Nombre total de points + rebonds BETCLIC":"","Nombre total de passes + rebonds BETCLIC":"","Nombre de passes décisives du joueur BETCLIC":"","Nombre total de rebonds du joueur":""
                name=item[0]['name'].split(' +')[0].split(' - Plus')[0]
                temp =[n["name"] for n in names]
                if name not in temp:
                    names.append({"name":name})
                    #print(name)
                data1.append({'name':name,'Total du joueur (points + rebonds + passes) BETCLIC':item[0]['name'].split(' + ')[-1].split('de ')[-1]})
            
        #print("----------")
        data2 = []
        if perf2 != []:
            perf2=perf2[0]
            for p in perf2['markets'][0]['selections']:
                name=p[0]['name'].split(' +')[0].split(' - Plus')[0]
                
                temp =[n["name"] for n in names]
                if name not in temp:
                    names.append({"name":name})
                
                data2.append({'name':name,"Total du joueur (points + passes) BETCLIC":(p[0]['name'].split(' + ')[-1].split('de ')[-1])})
               
        data3 = []
        if perf3 != []:
            perf3=perf3[0]
            for item in perf3['markets'][0]['selections']:
                
                name=item[0]['name'].split(' +')[0].split(' - Plus')[0]
                temp =[n["name"] for n in names]
                
                if name not in temp:
                    names.append({"name":name})
                data3.append({'name':name,"Nombre total de points + rebonds BETCLIC":(item[0]['name'].split(' + ')[-1].split('de ')[-1])})
        
        data4 = []
        if perf4 != []:
            perf4=perf4[0]
            for p in perf4['markets'][0]['selections']:
                name=p[0]['name'].split(' +')[0].split(' - Plus')[0]
                temp =[n["name"] for n in names]
                if name not in temp:
                    names.append({"name":name})
                data4.append({'name':name,"Nombre total de passes + rebonds BETCLIC":(p[0]['name'].split(' + ')[-1].split('de ')[-1])})
        data5 = []
        if perf5 != []:
            perf5=perf5[0]
            for p in perf5['markets'][0]['selections']:
                name=p[0]['name'].split(' +')[0].split(' - Plus')[0]
                temp =[n["name"] for n in names]
                if name not in temp:
                    names.append({"name":name})
                data5.append({'name':name,"Nombre de passes décisives du joueur BETCLIC":(p[0]['name'].split(' + ')[-1].split('de ')[-1])})
        data6 = []
        if perf6 != []:
            perf6=perf6[0]
            for p in perf6['markets'][0]['selections']:
                name=p[0]['name'].split(' +')[0].split(' - Plus')[0]
                temp =[n["name"] for n in names]
                if name not in temp:
                    names.append({"name":name})
                data6.append({'name':name,"Nombre total de rebonds du joueur BETCLIC":(p[0]['name'].split(' + ')[-1].split('de ')[-1])})
        #print(names)
        for item in names:
            index =[i for i in range(len(data1)) if data1[i]["name"]==item["name"]]
           
            if index != []:
                item['Total du joueur (points + rebonds + passes) BETCLIC']=data1[index[0]]['Total du joueur (points + rebonds + passes) BETCLIC']
            index1 =[i for i in range(len(data2)) if data2[i]["name"]==item["name"]]
            if index1 != []:
                item['Total du joueur (points + passes) BETCLIC']=data2[index1[0]]['Total du joueur (points + passes) BETCLIC']
            index2 =[i for i in range(len(data3)) if data3[i]["name"]==item["name"]]
            if index2 != []:
                item['Nombre total de points + rebonds BETCLIC']=data3[index2[0]]['Nombre total de points + rebonds BETCLIC']
            index3 =[i for i in range(len(data4)) if data4[i]["name"]==item["name"]]
            if index3 != []:
                item['Nombre total de passes + rebonds BETCLIC']=data4[index3[0]]['Nombre total de passes + rebonds BETCLIC']
            index4 =[i for i in range(len(data5)) if data5[i]["name"]==item["name"]]
            if index4 != []:
                item['Nombre de passes décisives du joueur BETCLIC']=data5[index4[0]]['Nombre de passes décisives du joueur BETCLIC']
            index5 =[i for i in range(len(data6)) if data6[i]["name"]==item["name"]]
            if index5 != []:
                item['Nombre total de rebonds du joueur BETCLIC']=data6[index5[0]]['Nombre total de rebonds du joueur BETCLIC']
                
                
        #print("---------------")
        
        
        df2 = pd.DataFrame(names)
        
        return df2
    except Exception as e:
        print(e)
        pass    #pprint(perf)
def UNIBET_m():
    
        res = requests.get('https://unibet.fr/zones/v3/sportnode/markets.json?nodeId=627956958&filter=R%25C3%25A9sultat&marketname=Vainqueur%2520(Prolongations%2520incluses)')
        data = pd.DataFrame(columns=['name', 'Total du joueur (points + rebonds + passes) UNIBET','Total du joueur (points + passes) UNIBET',"Nombre total de points + rebonds UNIBET","Nombre total de passes + rebonds UNIBET","Nombre de passes décisives du joueur UNIBET","Nombre total de rebonds du joueur UNIBET"])
        res =json.loads( res.content)
        i=0
        for link in res['marketsByType'][0]['days'][0]['events']:
            try : 
                
                #print(link['eventId'])
                rec= (UNIBET_per(link['eventId']))
                time.sleep(1)
                if len(rec):
                    data=data.append(rec,ignore_index=True)
                    
            except Exception as e:
                print(e)
                time.sleep(1)
                continue
        
        queue2.put(data)
    
def UNIBET_per(id):
    try:
        res = requests.get(f'https://unibet.fr/zones/event.json?eventId={id}')
        title= json.loads( res.content)['eventHeader']['name']
        #print(title)
        data1 = []
        
        perf1 = [perf for perf in json.loads( res.content)['marketClassList'] if perf["marketList"][0]['marketName']=="Performance du Joueur (Points + Rebonds + Passes)"]
        
        perf2 = [perf for perf in json.loads( res.content)['marketClassList'] if perf["marketList"][0]['marketName']=="Performance du Joueur (Points + Passes)"]
        #
        
        perf3 = [perf for perf in json.loads( res.content)['marketClassList'] if perf["marketList"][0]['marketName']=="Performance du Joueur (Points + Rebonds)"]
        
        perf4 = [perf for perf in json.loads( res.content)['marketClassList'] if perf["marketList"][0]['marketName']=="Performance du Joueur (Passes + Rebonds)"]
        
        perf5 = [perf for perf in json.loads( res.content)['marketClassList'] if perf["marketList"][0]['marketName']=="Nombre de passes du joueur"]
        
        perf6 = [perf for perf in json.loads( res.content)['marketClassList'] if perf["marketList"][0]['marketName']=="Nombre de rebonds du joueur"]
        
        names=[]
        if perf1 != []:
            perf1=perf1[0]
            for item in perf1['marketList'][0]['selections']:
                #,'Total du joueur (points + rebonds + passes) UNIBET':item[0]['name'].split('+ ')[-1].split('de ')[-1],"Total du joueur (points + passes) UNIBET":"","Nombre total de points + rebonds UNIBET":"","Nombre total de passes + rebonds UNIBET":"","Nombre de passes décisives du joueur UNIBET":"","Nombre total de rebonds du joueur":""
                
                if " - Plus" in item['name']:
                    name=item['name'].split(' - Plus')[0]
                    
                    temp =[n["name"] for n in names]
                    if name not in temp:
                        names.append({"name":name})
                        #print(name)
                    data1.append({'name':name,'Total du joueur (points + rebonds + passes) UNIBET':item['name'].split(' + ')[-1].split('de ')[-1]})
            
        #print("----------")
        data2 = []
        if perf2 != []:
            perf2=perf2[0]
            for p in perf2['marketList'][0]['selections']:
                if " - Plus" in p['name']:
                    name=p['name'].split(' - Plus')[0]
                    
                    temp =[n["name"] for n in names]
                    if name not in temp:
                        names.append({"name":name})
                    
                    data2.append({'name':name,"Total du joueur (points + passes) UNIBET":(p['name'].split(' + ')[-1].split('de ')[-1])})
                
        data3 = []
        if perf3 != []:
            perf3=perf3[0]
            for item in perf3['marketList'][0]['selections']:
                if " - Plus" in item['name']:
                    name=item['name'].split(' - Plus')[0]
                    temp =[n["name"] for n in names]
                    
                    if name not in temp:
                        names.append({"name":name})
                    data3.append({'name':name,"Nombre total de points + rebonds UNIBET":(item['name'].split(' + ')[-1].split('de ')[-1])})
        
        data4 = []
        if perf4 != []:
            perf4=perf4[0]
            for p in perf4['marketList'][0]['selections']:
                if " - Plus" in p['name']:
                    name=p['name'].split(' - Plus')[0]
                    temp =[n["name"] for n in names]
                    if name not in temp:
                        names.append({"name":name})
                    data4.append({'name':name,"Nombre total de passes + rebonds UNIBET":(p['name'].split(' + ')[-1].split('de ')[-1])})
        data5 = []
        if perf5 != []:
            perf5=perf5[0]
            for p in perf5['marketList'][0]['selections']:
                if " - Plus" in p['name']:
                    name=p['name'].split(' - Plus')[0]
                    temp =[n["name"] for n in names]
                    if name not in temp:
                        names.append({"name":name})
                    data5.append({'name':name,"Nombre de passes décisives du joueur UNIBET":(p['name'].split(' + ')[-1].split('de ')[-1])})
        data6 = []
        if perf6 != []:
            perf6=perf6[0]
            for p in perf6['marketList'][0]['selections']:
                if " - Plus" in p['name']:
                    name=p['name'].split(' - Plus')[0]
                    temp =[n["name"] for n in names]
                    if name not in temp:
                        names.append({"name":name})
                    data6.append({'name':name,"Nombre total de rebonds du joueur UNIBET":(p['name'].split(' + ')[-1].split('de ')[-1])})
        #print(names)
        for item in names:
            index =[i for i in range(len(data1)) if data1[i]["name"]==item["name"]]
           
            if index != []:
                item['Total du joueur (points + rebonds + passes) UNIBET']=data1[index[0]]['Total du joueur (points + rebonds + passes) UNIBET']
            index1 =[i for i in range(len(data2)) if data2[i]["name"]==item["name"]]
            if index1 != []:
                item['Total du joueur (points + passes) UNIBET']=data2[index1[0]]['Total du joueur (points + passes) UNIBET']
            index2 =[i for i in range(len(data3)) if data3[i]["name"]==item["name"]]
            if index2 != []:
                item['Nombre total de points + rebonds UNIBET']=data3[index2[0]]['Nombre total de points + rebonds UNIBET']
            index3 =[i for i in range(len(data4)) if data4[i]["name"]==item["name"]]
            if index3 != []:
                item['Nombre total de passes + rebonds UNIBET']=data4[index3[0]]['Nombre total de passes + rebonds UNIBET']
            index4 =[i for i in range(len(data5)) if data5[i]["name"]==item["name"]]
            if index4 != []:
                item['Nombre de passes décisives du joueur UNIBET']=data5[index4[0]]['Nombre de passes décisives du joueur UNIBET']
            index5 =[i for i in range(len(data6)) if data6[i]["name"]==item["name"]]
            if index5 != []:
                item['Nombre total de rebonds du joueur UNIBET']=data6[index5[0]]['Nombre total de rebonds du joueur UNIBET']
                
                
        #print("---------------")
        
        
        df2 = pd.DataFrame(names)
        
        return df2
    except Exception as e:
        print(e)
        pass    #pprint(perf)
    

def compare(data):
    perf1= "Performance du joueur (Points+ Rebonds + Passes)"
    perf2 = "Total du joueur (points + passes)"
    perf3="Total du joueur (points + rebonds)"
    perf4="Total du joueur (passes + rebonds)"
    perf5="Nombre de passes décisives du joueur"
    perf6="Nombre de rebonds du joueur"
    def message(perf,match,player,winamax,betclic,unibet):
        
                message = '''{} Match {} {}

                Winamax : {} 
                Betclic : {}
                Unibet  : {}
                    '''.format(perf,match,player,str(winamax),str(betclic),str(unibet))
            
                base_url = 'https://api.telegram.org/bot5029164355:AAFzg0voW4nMwyeDL4ictvNuGo4_rNPHA7k/sendMessage?chat_id=-1001630243175&text={}'.format(message)
                requests.get(base_url)
           
                
                
                
    def Cuts_Diff(x):
            data= [(x['Total du joueur (points + rebonds + passes) WINAMAX']), (x['Total du joueur (points + rebonds + passes) BETCLIC']),(x['Total du joueur (points + rebonds + passes) UNIBET'])]
            data = pd.DataFrame(data)
            temp=data.dropna()
 
            if  (data.duplicated()).sum() + (data.isnull().sum())[0] <2 :
                message(perf1,x['titre'],x['name'],data.iloc[0][0],data.iloc[1][0],data.iloc[2][0])
            data= [(x['Total du joueur (points + passes) WINAMAX']), (x['Total du joueur (points + passes) BETCLIC']), (x['Total du joueur (points + passes) UNIBET'])]
            data = pd.DataFrame(data)
            temp=data.dropna()
            if  (data.duplicated()).sum() + (data.isnull().sum())[0] <2 :
                message(perf2,x['titre'],x['name'],data.iloc[0][0],data.iloc[1][0],data.iloc[2][0])
            data= [(x['Total du joueur (points + rebonds) WINAMAX']), (x['Nombre total de points + rebonds BETCLIC']), (x['Nombre total de points + rebonds UNIBET'])]
            data = pd.DataFrame(data)
            temp=data.dropna()
            if  (data.duplicated()).sum() + (data.isnull().sum())[0] <2 :
                message(perf3,x['titre'],x['name'],data.iloc[0][0],data.iloc[1][0],data.iloc[2][0])
            data= [(x['Total du joueur (passes + rebonds) WINAMAX']), (x['Nombre total de passes + rebonds BETCLIC']), (x['Nombre total de passes + rebonds UNIBET'])]
            data = pd.DataFrame(data)
            temp=data.dropna()
            if  (data.duplicated()).sum() + (data.isnull().sum())[0] <2 :
                message(perf4,x['titre'],x['name'],data.iloc[0][0],data.iloc[1][0],data.iloc[2][0])
            data= [(x['Nombre de passes décisives du joueur WINAMAX']), (x['Nombre de passes décisives du joueur BETCLIC']), (x['Nombre de passes décisives du joueur UNIBET'])]
            data = pd.DataFrame(data)
            temp=data.dropna()
            if  (data.duplicated()).sum() + (data.isnull().sum())[0] <2 :
                message(perf5,x['titre'],x['name'],data.iloc[0][0],data.iloc[1][0],data.iloc[2][0])
            data= [(x['Nombre de rebonds du joueur WINAMAX']), (x['Nombre total de rebonds du joueur BETCLIC']), (x['Nombre total de rebonds du joueur UNIBET'])]
            data = pd.DataFrame(data)
            temp=data.dropna()
            if  (data.duplicated()).sum() + (data.isnull().sum())[0] <2 :
                message(perf6,x['titre'],x['name'],data.iloc[0][0],data.iloc[1][0],data.iloc[2][0])
            
                
    
    data['Col1'] = data.apply(lambda x: Cuts_Diff(x),axis=1)





def removeNan(array1):
    nan_array = np.isnan(array1)
    not_nan_array = ~ nan_array
    array2 = array1[not_nan_array]
    return array2.size()



from functools import reduce

if __name__ == '__main__':
    #f = open("set.txt", "r")
    i=0
    data= pd.DataFrame()
    while True:
        try :
            if i==0:
                queue1 = queue.Queue()
                thread_ = threading.Thread(
                                target=betclic_m,
                                name="Thread1",
                                
                                )
                
                
                
                
                queue2 = queue.Queue()
                thread_2 = threading.Thread(
                                target=UNIBET_m,
                                name="Thread2",
                                
                                )
                thread_2.start()
                thread_.start()
                thread_.join()
                thread_2.join()
                
                
                return_val2 = queue2.get()
                return_val = queue1.get()
                r2=get_matches()
              
                
                dfs=[return_val,return_val2,r2]
                data = reduce(lambda left,right: pd.merge(left,right,on='name'), dfs)
                #result.drop(columns=['titre_x'])
                message = '''---------------------- UPDATE (*) ----------------------'''
                
                base_url = 'https://api.telegram.org/bot5029164355:AAFzg0voW4nMwyeDL4ictvNuGo4_rNPHA7k/sendMessage?chat_id=-YOURID&text={}'.format(message)
                requests.get(base_url)
                #with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
                
                compare(data)
                time.sleep(3)
                i=1
            else:
                queue1 = queue.Queue()
                thread_ = threading.Thread(
                                target=betclic_m,
                                name="Thread1",
                                
                                )
                
                
                
                
                queue2 = queue.Queue()
                thread_2 = threading.Thread(
                                target=UNIBET_m,
                                name="Thread2",
                                
                                )
                thread_2.start()
                thread_.start()
                thread_.join()
                thread_2.join()
                
                
                return_val2 = queue2.get()
                return_val = queue1.get()
                r2=get_matches()
                dfs=[return_val,return_val2,r2]
                new = reduce(lambda left,right: pd.merge(left,right,on='name'), dfs)
                #result.drop(columns=['titre_x'])
                new = pd.concat([data,new])

                new.drop_duplicates(keep = False, inplace = True)
                
                if not new.empty:
                    data=pd.concat([data,new])
                    message = '''---------------------- UPDATE ----------------------'''
                    
                    base_url = 'https://api.telegram.org/bot5029164355:AAFzg0voW4nMwyeDL4ictvNuGo4_rNPHA7k/sendMessage?chat_id=-YOURID&text={}'.format(message)
                    requests.get(base_url)
                    
                    
                    
                    compare(new)
                    time.sleep(3)
        except Exception as e:
            print(e)
            continue