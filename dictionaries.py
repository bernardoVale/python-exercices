import fib

foo = {
    'fruit': 'banana',
    'pi': 3.14,
}

import json

content = json.dumps(foo)

print(content)

with open('fruits.json', 'w') as stream:
    json.dump(foo, stream, indent=4)