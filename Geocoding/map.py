# Reads in a CSV file of locations, in this case the lat/lon of volcanoes in the US, and 
# returns an HTML page with markers on an interactive map
import folium
import pandas

data = pandas.read_csv("Geocoding/Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elevation = list(data["ELEV"])

# Returns different colors for the icons depending on the height of the volcano
def color_gen(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

# Volcanoes
fgv = folium.FeatureGroup(name="Volcanoes")

# Loops through the input file and rips out the name, location, and elevation of the volcanoes
# Sanitizes the name field for names with single quotes in them
for lt,ln,na, el in zip(lat, lon, name, elevation):
    fgv.add_child(folium.Marker(location=[lt, ln], popup="{}, at {} m".format(na.replace("'", r"\'"),el), icon=folium.Icon(color=color_gen(el))))

# Populations around the world
fgp = folium.FeatureGroup(name="Population")

# Adds borders to major countries around the world & shades in colors depending on population
fgp.add_child(folium.GeoJson(data=open("Geocoding/world.json", "r", encoding="utf-8-sig").read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Add different layers for LayerControl()
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Geocoding/Map1.html")