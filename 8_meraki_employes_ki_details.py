import json
list1=["neelam","programer","2","2400"]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"]  
list5=["name","designation","age","salary"]
dict1=dict(zip(list5,list1))
print(dict1)
dict2=dict(zip(list5,list2))
print(dict2)
dict3=dict(zip(list5,list3))
print(dict3)
dict4=dict(zip(list5,list4))
print(dict4)
d={}
for key,value in dict1.items():
    d["emp1"]=dict1
    for key,value  in dict2.items():
        d["emp2"]=dict2
        for key,value in dict3.items():
            d["emp3"]=dict3
            for key,value  in dict4.items():
                d["emp4"]=dict4
print()

# print(d)
json_object = json.dumps(d, indent = 4)
print(json_object)
