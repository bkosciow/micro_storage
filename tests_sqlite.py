from src.micro_storage.storage import Storage
from src.micro_storage.sqlite_engine import SQLiteEngine
import random
import string
import pprint

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


Storage.set_engine(SQLiteEngine())
storage = Storage()

print("* basic values:")
name = get_random_string(12)

print(storage.exists(name))
assert storage.exists(name) is False
storage.set(name, 'meow')
print(storage.get(name))
assert storage.get("nonexistent") is None
assert storage.get(name) == "meow"
storage.set(name, 'meow123')
print(storage.get(name))
assert storage.get(name) == "meow123"
print(storage.exists(name))
assert storage.exists(name) is True

print("* dict/list values:")
data1 = ['abc', 13, 'def', 15]
data2 = {'name': 'meow', 'count': 99}
data3 = {'a1': [1,2,3], 'a2': {'a': 1, 'b':2}}

name = get_random_string(12)

assert storage.exists(name) is False
storage.set(name, data1)
assert storage.exists(name) is True
pprint.pprint(storage.get(name))
assert type(storage.get(name)) is list
assert storage.get(name)[0] == 'abc'


name = get_random_string(12)

assert storage.exists(name) is False
storage.set(name, data2)
assert storage.exists(name) is True
pprint.pprint(storage.get(name))
assert type(storage.get(name)) is dict
assert storage.get(name)['name'] == 'meow'


name = get_random_string(12)

assert storage.exists(name) is False
storage.set(name, data3)
assert storage.exists(name) is True
pprint.pprint(storage.get(name))
assert type(storage.get(name)) is dict
assert storage.get(name)['a1'][0] == 1