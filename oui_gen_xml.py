import requests 
import xml.etree.ElementTree as ET
res = {} 
  
ouis  = requests.get("https://standards-oui.ieee.org").text 
for line in ouis.split("\n"): 
    hex,spl,name = line.strip("\n").partition("(base 16)")
    if spl : 
        if name.strip() in res : 
            res[name.strip()].append(hex.strip())
        else : 
             res[name.strip()] = [hex.strip()]
             
xml_data = ET.Element("oui_list")
for name,lst in res.items() : 
    mani = ET.Element("manufacturer")
    mani.set("name",name)
    for oui in lst : 
        ouiET = ET.Element("hex")
        ouiET.text = oui 
        mani.append(ouiET)
    xml_data.append(mani)
    


with open("ouilist.xml",'wb') as file : 
    file.write(ET.tostring(xml_data))