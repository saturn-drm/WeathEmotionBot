#%%
# the script is written in jupyter notebook via VSCODE
import json
# %%
# read city list json file to dict
# parse the file to simplified text
initjsonpath = 'current.city.list.json'
with open(initjsonpath) as f:
    initjson = json.load(f)

initjson[0]['name']
#%%
type(initjson)
# %%
citystr = ''
for city in initjson:
    citystr += city['name']
    citystr += ' '
citystr
# %%
outf = open('citysimplified.txt', 'w')
outf.write(citystr)
outf.close()
# %%
