
import geopandas as gp
import json
from shapely.geometry import Point 

def makePoint(city):
  feature = {
    "type": "Feature",
    "properties": {
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



with open('cities.json') as f:
    cities = json.load(f)

with open('states.geojson') as s:
    states = json.load(s)
  
stateDict = {}
states = states["features"]



for state in states:
    state['properties']['title'] = state['properties']['name'] 
    state['properties']['stroke'] = "#000000" 
    state['properties']['fill'] = '#F5F5F5' 
    state['properties']['stroke-width'] = 1 
    state['properties']['population'] = 0 
    stateDict[state['properties']['name']] = 0

#reads geoseries in 
with open('states.geojson') as s:
    gp_states = gp.read_file(s)


#Contains the polygon for each state
gp_series = gp.GeoSeries(gp_states['geometry'])


pointfeat = []

for i in range(len(cities)): # loop through the cities
  if cities[i]['longitude'] > -140:


    points = Point(cities[i]['longitude'],cities[i]['latitude'])

    PointQuery = gp_series.sindex.query(points, predicate='within')
    if PointQuery.size == 1:

        stateDict[states[PointQuery.item(0)]['properties'] \
            ['name']] += cities[i]['population']


for k, v in stateDict.items(): 
    for data in states: 
        if data['properties']['name'] == k:
            data['properties']['population'] = v 
            
            

            # compare the value of color based on popu size
            if v < 20000000  and v >= 15000000: 
                        data['properties']['fill'] = '#D2E6F9' 
            elif v < 15000000 and v >= 10000000: 
                        data['properties']['fill'] = '#FFF217'
            elif v < 10000000 and v >= 9000000: 
                        data['properties']['fill'] = '#FFA156'
            elif v < 9000000 and v >= 8000000: 
                        data['properties']['fill'] = '#00993' 
            elif v < 8000000 and v >= 7000000: 
                        data['properties']['fill'] = '#000FFE'     
            elif v < 7000000 and v >= 6000000: 
                        data['properties']['fill'] = '#919900' 
            elif v < 6000000 and v >= 5000000: 
                        data['properties']['fill'] = '#FA0A0A' 

            elif v < 5000000 and v >= 4000000:
                        data['properties']['fill'] = '#F610E7' 
            elif v < 4000000 and v >= 3000000: 
                        data['properties']['fill'] = '#025E4D'      
            elif v < 3000000 and v >= 2000000: 
                        data['properties']['fill'] = '#5E8F18'
            elif v < 2000000 and v >= 1000000: 
                        data['properties']['fill'] = '#7B2A74'
            elif v < 1000000 and v >= 500000: 
                        data['properties']['fill'] = '#F012FF' 
            elif v < 500000 and v >= 250000:
                        data['properties']['fill'] = '#EE28B6'  
            elif v < 250000 and v >= 100000:          
                        data['properties']['fill'] = '#77EE28'
            
            elif v < 100000: #
                        data['properties']['fill'] = '#45255F' 
            else: 
                        data['properties']['fill'] = '#000000'
                        


GeoJsonOutput = {
            "type": "FeatureCollection",
            "features": []
         }
for s in states:
    GeoJsonOutput['features'].append(s)

for p in pointfeat:
    GeoJsonOutput['features'].append(p)

with open('result.geojson', 'w') as o:
      o.write(json.dumps(GeoJsonOutput, indent=4))

