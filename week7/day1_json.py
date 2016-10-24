l = ["5","connor",None,4]

string_list = str(l)

print(string_list)

import json
json_list = json.dumps(l)
print(json_list)
print(json.dumps({"connor": '1'}))
