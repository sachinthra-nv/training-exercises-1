
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
            # print(newKeys)
            if 'image' in newKeys:
                print("woooooow: ",dc[i]['image'])
            findImageTag(dc[i],newKeys)
        elif type(dc[i]) is list:
            for j in dc[i]:
                if type(j) is not str:
                    newKeys = list(j.keys())
                    if 'image' in newKeys:
                        print("wooooooow: ",j['image'])
                    findImageTag(j,newKeys)
        
    return