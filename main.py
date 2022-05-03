import json
import random
from fileinput import close
from collections import defaultdict

def randColor():
  r = lambda: random.randint(0,255)
  return ('#%02X%02X%02X' % (r(),r(),r()))

FeatureCollection = {}
FeatureCollection["type"] = "FeatureCollection"
FeatureCollection["features"] = []


def makePoint(city):
  feature = {
    "type": "Feature",
    "properties": {
      "marker-color":randColor(),
      "marker-size" : "small",
      "marker-symbol": '1'
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0,0]
    }   
  }


  for key,val in city.items():

    if key == 'latitude':
      feature['geometry']['coordinates'][1] = val
    elif key == 'longitude':
      feature['geometry']['coordinates'][0] = val
    else:
        feature['properties'][key] = val
    

  return feature



def makeLineString(leftside):
    feature = {
      "type": "Feature",
      "properties": {
        "color":randColor(),
      },
      "geometry": {
        "type": "LineString",
        "coordinates": 
        
          startline
        
      }
    }

  


    return feature
    



with open("cities.json") as f:
  data = json.load(f)

largestCities = [] 
sortedData = []
d = defaultdict(dict)
sortedData = sorted(data, key= lambda x: x['population'], reverse=True)


newStates = ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Washington DC', 'Delaware', 'Florida', 'Georgia',  'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

temp=[] 
for i in sortedData:
  for x in newStates:
    if i["state"] == x and i["state"] not in temp:
      temp.append(i["state"])
      largestCities.append(i)
      break

for i in largestCities:
    d[i["state"]].update(i)
        


#for key,value in d.items():
 # if key == "state":
  ###  d[key["population"]].update(x) 

    

with open("output.json", 'w') as output_file:
    json.dump(list(d.values()), output_file, indent=4)

with open ("output.json") as f:
    refinedData = json.load(f)

f.close()
#with open("output.json") as f:
  #refinedData = json.load(f)

#points = []



close_cities_Data = []
#sorts the states by closest 
n = defaultdict(dict)
close_cities_Data = sorted(refinedData, key= lambda x: x['longitude'], reverse=True)
# add the rank for each city
rank = 1
for item in close_cities_Data:
    item['rank'] = rank
    rank +=1



for i in close_cities_Data:
    n[i["state"]].update(i)

        

with open("new.json",'w') as output_file:
  json.dump(list(n.values()), output_file, indent=4)



with open("new.json") as f:
  refinedData= json.load(f)

#for stateInfo in refinedData:
    #if "Hawaii" not in stateInfo.values() and "Alaska" not in stateInfo.values():
        #FeatureCollection["features"].append(makePoint(stateInfo))



startline = []

for i in range(len(refinedData)-1):   
  startline.append( [refinedData[i]["longitude"], refinedData[i]["latitude"]])
  startline.append([refinedData[i+1]["longitude"], refinedData[i+1]["latitude"]])
    
for stateInfo in refinedData:
    FeatureCollection["features"].append(makePoint(stateInfo))
 


FeatureCollection["features"].append(makeLineString(startline))

with open("refinedData1.json","w") as f:
  json.dump(FeatureCollection,f,indent=4)
  
