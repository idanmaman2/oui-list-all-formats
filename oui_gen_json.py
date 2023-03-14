import requests 
import json
res = {}     
ouis  = requests.get("https://standards-oui.ieee.org").text 
for line in ouis.split("\n"): 
    hex,spl,name = line.strip("\n").partition("(base 16)")
    if spl : 
        if name.strip() in res : 
            res[name.strip()].append(hex.strip())
        else : 
             res[name.strip()] = [hex.strip()]

with open("ouilist.json",'w') as file : 
    json.dump(res,file)