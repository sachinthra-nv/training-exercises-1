# # import pyyaml module
# import yaml
# from yaml.loader import SafeLoader

# # Open the file and load the file
# with open('capk.yaml') as f:
#     data = yaml.load(f, Loader=yaml.load_all)
#     print(data)

import yaml

from yaml.loader import SafeLoader

with open('capk.yaml', 'r') as f:
    data = list(yaml.load_all(f, Loader=SafeLoader))
    print(data)