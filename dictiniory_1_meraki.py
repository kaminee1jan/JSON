import json
dict1='{"name":"ram","class":"iv","age":9}'
json_object = json.loads(dict1)
print(json_object)

# "json to python convert"

import json
a = {"name" : "GeeksforGeeks", "Topic" : "Json to String", "Method": 1}
# Convert JSON to String
y = json.dumps(a)
print(y)
print(type(y))


