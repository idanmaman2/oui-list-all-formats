import requests 
import yaml
res = {}     
ouis  = requests.get("https://standards-oui.ieee.org").text 
for line in ouis.split("\n"): 
    hex,spl,name = line.strip("\n").partition("(base 16)")
    if spl : 
        if name.strip() in res : 
            res[name.strip()].append(hex.strip())
        else : 
             res[name.strip()] = [hex.strip()]
with open("ouilist.yaml",'w') as file : 
    yaml.dump(res,file)