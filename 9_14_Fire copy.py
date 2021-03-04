import json

infile = open('US_fires_9_14.json', 'r')
outfile = open('readable_9_14_data.json', 'w')

fire_data = json.load(infile)

json.dump(fire_data, outfile, indent=4)


brightness, lons, lats = [],[],[]
for fire in fire_data:
    bright= fire['brightness']
    lat = fire['latitude']
    lon = fire['longitude']
    brightness.append(bright)
    lats.append(lat)
    lons.append(lon)

from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

data = [
    {
        'type': 'scattergeo',
        'lat': lats,
        'lon': lons,
        "marker": {
            'color': brightness,
            'colorscale': "Viridis"
            'reversescale': True,
            'colorbar':{'title': 'Brightness'},
        }
    }
]

my_layout = Layout(title = "California Fires 9/1-9/13")
fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename= 'cali_fires_9_1.html')
