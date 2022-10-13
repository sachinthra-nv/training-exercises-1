

import yaml
from yaml.loader import SafeLoader
from functions.functions import *

# globals
the_key = 'image'

# Reading Yaml File to a Dict
with open('capk.yaml', 'r') as f:
    data = list(yaml.load_all(f, Loader=SafeLoader))
    for dc in data:
        forEachDict(dc)
    # print(data[0].keys())
    # key_index = list(data[0]).index(the_key) if the_key in data[0] else None
    # print(key_index)
    # if 'kind' in data[0]:
    #     print(list(data[0]).index('kind'))


# Writing Dict Data to Yaml File
# with open('temp.yaml', 'w') as f:
#     data = yaml.dump_all(data, f, sort_keys=False, default_flow_style=False)
