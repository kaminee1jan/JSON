import json
dict1={
    "name":"ram",
    "class":"iv",
    "age":9
}
dic=json.dumps(dict1)
print(dic)
json_object = json.dumps(dict1,indent=3)
print(type(json_object))
with open("dictiniory.json", "w") as outfile:
    outfile.write(json_object)


# "python to Json convert"