
def forEachDict(dc):
    keys = list(dc.keys())
    # print(keys)
    findImageTag(dc, keys)

def findImageTag(dc,keys):
    for i in keys:
        # print(i)
        # print(type(dc[i]) is list or type(dc[i]) is dict)
        if(type(dc[i]) is dict):
            # print(dc[i])
            newKeys = list(dc[i].keys())
            print(newKeys)
            if 'image' in newKeys:
                print(dc[i])
            findImageTag(dc[i],newKeys)
        
    return