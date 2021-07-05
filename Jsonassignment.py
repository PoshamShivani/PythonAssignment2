import json
Normal_str = {'4': 5, '6': 7, '1': 3, '2': 4,'3':9}
print("Converted JSON data:")
print(json.dumps(Normal_str, sort_keys=True, indent=4))