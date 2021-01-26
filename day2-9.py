dic1={"a":'apple',"c":'ccc',"e":"eee"}
dic1["d"]='dog'
print(dic1)
for key in dic1.values():
    print(key)
for k,v in dic1.items():
    print(k,"=>",v)