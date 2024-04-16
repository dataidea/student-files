import json

# JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Parsing the JSON string into a Python dictionary using json.loads()
parsed_dict = json.loads(json_string)

print("Parsed dictionary:", parsed_dict)
