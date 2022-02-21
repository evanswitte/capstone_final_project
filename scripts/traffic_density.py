# imports
import json
import time as tm

import pandas as pd
from tqdm import tqdm

# input to get the json file and how and were it will be safed
geojson = input('Put the name.json in here: ')
path=input('Enter the path were u want to save on your machine: ')
name_the_file = input('Name the file: ')

# open the json and save in a variable
f = open(geojson)
data = json.load(f)

# normalize the json to get a dataframe
density = pd.json_normalize(data, sep="_")

# create new columns from network_segmentRules which is in a dictoinary
# put all in new list to take them later for a new dataframe

id = []
Newid = []
speedLimit = []
frc = []
streetName = []
distance = []
shape = []
segmentTimeResults = []
sampleSize = []
harmonicAverageSpeed = []
for a in density["network_segmentResults"][0]:
    id.append(a.get('segmentId', None))
    Newid.append(a.get('newSegmentId', None))
    speedLimit.append(a.get('speedLimit', None))
    frc.append(a.get('frc',None))
    streetName.append(a.get('streetName',None))
    distance.append(a.get('distance',None))
    shape.append(a.get('shape',None))
    segmentTimeResults.append(a.get('segmentTimeResults',None))
    
for a in segmentTimeResults:
        for i in a:
            sampleSize.append(i.get('sampleSize', None))
            harmonicAverageSpeed.append(i.get('harmonicAverageSpeed',None))

# create the new dataframe with the new columns    
network = pd.DataFrame({
    'id': id,
    'newid': Newid,
    "speedLimit":speedLimit,
    "frc":frc,
    "streetName":streetName,
    "distance":distance,
    "shape":shape,
    "sampleSize":sampleSize,
    "harmonicAverageSpeed":harmonicAverageSpeed
})

network.drop(network[(network.frc == 0) & (network.speedLimit >= 100)].index, inplace=True)

# reset the index and safe it as a csv
network.to_csv(f'{path}{name_the_file}.csv')

# time to see that the upload is succesful
for i in tqdm(range(100)):
    tm.sleep(0.003)
