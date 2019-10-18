import folium
import geoip2.database
def readIP():
    lines = []
    with open("testip.txt") as file:
        for line in file: 
            line = line.strip() 
            lines.append(line) 
    return lines
caption =''
reader = geoip2.database.Reader("GeoLite2-City.mmdb")
iplist = readIP()
m = folium.Map(location=[0,0], 
                zoom_start=3, control_scale=True, prefer_canvas=True)
for ip in iplist:
    if ip:
        record  = reader.city(ip)

        if record.location.latitude:
                
            popup      = folium.Popup(caption+ip)
            marker = folium.Marker([record.location.latitude,record.location.longitude],popup=popup)
                
            m.add_child(marker)
outfp = "map.html"

# Save the map
m.save(outfp)
