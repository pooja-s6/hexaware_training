import json
 
student = {
    "name": "Alice",
    "age": 22,
    "courses": ["Math", "Science"],
    "is_graduated": False
}
 
print(student)
 
json_str = json.dumps(student)
print(type(json_str))
print(json.loads(json_str))
#pretty print
print(json.dumps(student, indent=2))