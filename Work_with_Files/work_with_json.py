import json
from json import JSONDecodeError


json_string = '{"a": "apple", "b": "bear", "c": "cat", }'
try:
    print(json.loads(json_string))
except JSONDecodeError:
    print('Could not parse JSON!')

python_dict = {"a": "apple", "b": "bear", "c": "cat", }
print(json.dumps(python_dict))
