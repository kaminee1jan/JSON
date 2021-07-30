import json
dict={

    "shopping_list":
        { 
            "chaco":15,
            "Biscuits":50,
            "Diary_milk":30,
            "ice_cream":20,
        } 
}
dic=json.dumps(dict)
json_object=json.dumps(dict,indent=4)
with open("dict.json","w") as outfile:
    outfile.write(json_object)
items=input("which items you want")
quantity=int(input("how many items you want"))
for key in dict:
    for i in dict[key]:
        if i==items:
            dict[key][i]=(dict[key][i]-quantity)
print(json.dumps(dict,indent=4))
