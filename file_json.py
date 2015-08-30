import json

input_file = open("/Users/wanyizhou/Documents/Workspace/Python/json_cleanup",'r')
name = "Door btw b4 and b5"

def tuple_to_dict(the_tuple):
    eachDict = {}
    for i in the_tuple:
        key,value= i.strip().split(":")
        if 'B' in value:
            value = int(value[-1].strip())
        else:
            value = int(value.strip())
        eachDict[key] = int(value)
    eachDict['sum'] =sum(eachDict.values()[1:])
    return eachDict

list_of_dicts = []
count = ['count:' + str(x) for x in range(1,121)]
lines_iter = iter(input_file)

for pri_sec_region in zip(lines_iter, lines_iter, lines_iter,count):
    print pri_sec_region
    list_of_dicts.append(tuple_to_dict(pri_sec_region))


print list_of_dicts
                        
###jsonfile = open('/Users/wanyizhou/Documents/Workspace/Python/data.json','w')
jsonfile = open('/Users/wanyizhou/Documents/Workspace/YourMove/Test_data_graph/data/data.json','w')
json.dump(list_of_dicts, jsonfile)
jsonfile.close()
