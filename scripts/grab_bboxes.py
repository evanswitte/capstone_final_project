import requests
import json
import pandas as pd
from pandas import json_normalize
from api_key import api_key 
# Berlin
b_box1=['52.6631698085311, 13.140242153972684','52.558969401173485, 13.327137463439458']
b_box2=['52.66583302519144, 13.328187843937375','52.55975760033779, 13.531524756658655']
b_box3=['52.662667235053135, 13.525254267127615','52.55871840688914, 13.694268779933639']
b_box4=['52.55550179023949, 13.13837075539878','52.471124761327616, 13.332537006109098']
b_box5=['52.55739063388284, 13.332348357156704','52.47191079948233, 13.528715628184314']
b_box6=['52.55500988551918, 13.53021147822543','52.47243768064713, 13.697637276886649']
b_box7=['52.46527785814766, 13.141568901913262','52.38090146182574, 13.332728391245771']
b_box8=['52.46796014971922, 13.3338429398249','52.382480041632, 13.527216204640395']
b_box9=['52.46557494099577, 13.53389728381432','52.379044975931045, 13.69577591550085']

#hamburg
h_box1=['53.73006536457588, 9.727426746670874','53.60686979447982, 9.939483076656447']
h_box2=['53.73043682011384, 9.94337071142755','53.6068907762533, 10.142079060308985']
h_box3=['53.73128846532158, 10.142350061467159','53.608968874508165, 10.388345220828366']
h_box4=['53.60397120239643, 9.722804283417556','53.50836764305371, 9.938345776491245']
h_box5=['53.605201539781724, 9.940894562090719','53.510059963971116, 10.141875342699002']
h_box6=['53.607727561051775, 10.139266919037887','53.50879262755643, 10.386144578696795']
h_box7=['53.5075456575369, 9.95238438851308','53.40404578237425, 10.134658131061412']
h_box8=['53.50755572879408, 10.141870158046851','53.40110835001105, 10.379717528781294']

#köln
k_box1=['51.017821350032314, 6.82445640264807','50.94210364737058, 6.977208131229709']
k_box2=['51.017943689941795, 6.976369794960072','50.94154890547941, 7.107196501571785']
k_box3=['50.94096441056806, 6.823945241836748','50.867779116006105, 6.97643958860067']
k_box4=['50.94210364737058, 6.977208131229709','50.86773302756594, 7.102220047380358']

#frankfurt
f_box1=['50.191104520159705, 8.53586131886934','50.11446163078797, 8.684995063104202']
f_box2=['50.18920487383416, 8.686536354040065','50.1154266671422, 8.812579471619806']
f_box3=['50.113328014694794, 8.536932829888363','50.038707864191636, 8.686602980509065']
f_box4=['50.11446163078797, 8.684995063104202','50.03967256223699, 8.810844779852912']

#münchen

m_box1=['48.23332659692213, 11.394125178952903','48.13458469204817, 11.584600062317453']
m_box2=['48.23979136937424, 11.58663342658928','48.134506750200906, 11.749546487080057']
m_box3=['48.132971243850456, 11.38623920063464','48.03007286311463, 11.58361407489094']
m_box4=['48.13458469204817, 11.584600062317453','48.02998966403243, 11.751359256966808']

poi=input('What are you looking for? Please enter a place: ')
path=input('enter the path: ')
city_loop=[b_box1,b_box2,b_box3,b_box4,b_box5,b_box6,b_box7,b_box8,b_box9,h_box1,h_box2,h_box3,h_box4,h_box5,h_box6,h_box7,h_box8,k_box1,k_box2,k_box3,k_box4,f_box1,f_box2,f_box3,f_box4,m_box1,m_box2,m_box3,m_box4]
count=0
for l in city_loop:
    count+=1
    binboxes=[l]
    file_name=f'{poi}{count}'
    # input the relevant information

    for i in binboxes:
        topleft=i[0]
        btmright=i[1]

        # change variables to fit in url
        topleft_=[]
        for i in topleft:
            if i != ',':
                topleft_.append(i)
            else:
                topleft_.append('%2C')
        topleft=''.join(topleft_).replace(' ','')

        btmright_=[]
        for i in btmright:
            if i != ',':
                btmright_.append(i)
            else:
                btmright_.append('%2C')
        btmright=''.join(btmright_).replace(' ','')

        #create url
        limit='100'
        url = f"https://api.tomtom.com/search/2/poiSearch/{poi}.json?limit={limit}&topLeft={topleft}&btmRight={btmright}&view=Unified&relatedPois=off&key={api_key}"
        payload={}
        headers = {}

        # get data
        response = requests.get(url, headers=headers, data=payload)

        # flatten json
        traffic=response.json()

        df_normalized=pd.json_normalize(traffic)

        FIELDS=['results']
        dt=df_normalized[FIELDS]

        dt=dt.explode('results')

        df_final=(pd.DataFrame(dt['results'].apply(pd.Series)))

        # data cleaning
        df_final['address']
        new=pd.DataFrame.from_dict(df_final['address'])

        name=[]
        for i in df_final['poi']:
            for key, value in i.items():
                if key=='name':
                    name.append(value)
        new['name']=name

        address=[]
        Postcode=[]
        for i in new['address']:
            for key, value in i.items():
                if key=='freeformAddress':
                    address.append(value)
                if key=='postalCode':
                    Postcode.append(value)
        new['addresses']=address
        new['Postcode']=Postcode

        latitude=[]
        longitude=[]
        for i in df_final['position']:
            for key, value in i.items():
                if key=='lat':
                    latitude.append(float(value))
                if key=='lon':
                    longitude.append(float(value))
        new['latitude']=latitude
        new['longitude']=longitude

        df=new[['name','addresses','Postcode','latitude','longitude']]
        df.columns=['name','address','postcode','lat','long']
        num=len(df['name'])
        print('')
        print(f'imported {num} places in {file_name} to {path} in file {count}')

        #export to csv
        df.to_csv(f'{path}{file_name}.csv', header=True) 
#data cleaning
df=0
x={}
for i in range(29):
    x[i]=pd.read_csv(f'{path}{poi}{i+1}.csv')

df=pd.concat([x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19], x[20], x[21], x[22], x[23], x[24], x[25], x[26], x[27], x[28]])

df=df[['name','address','postcode','lat','long']]

df.columns=['name', 'address','postcode','latitude','longitude']

polygon=pd.read_csv('/Users/andrekiehm/Documents/neuefische/Capstone/Polygons/polygon_data.csv')
polygon.head()
plz=[]
tf=[]
for i in polygon['Postcode']:
    plz.append(i)
for d in df['postcode']:
    if d in plz:
        tf.append(True)
    else:
        tf.append(False)
df['filter']=tf

df=df[df['filter']==True]

df=df[['name','address','postcode','latitude','longitude']]

df.to_csv(f'{path}{poi}_final.csv', header=True) 