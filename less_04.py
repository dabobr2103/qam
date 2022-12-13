
users_dict = {
    "first": {"name": "Alex", "password": "qwert1234"},
    "second": {"name": "Olga", "password": "123qwert4"},
    "third": {"password": "123qwert4"}
    }
number_set = {1,2,3,5}

# print(users_dict["second"]["name"])
# print(users_dict.get("third").get("name", "Vasik"))
#iter dict - default is key only
for k in users_dict:
    print(k)
#iter dict - get values metod:
for v in users_dict.values():
    print(v)
# OR
for k in users_dict:
    print(users_dict[k])
#iter dict - get items (key and values)
for k, v in users_dict.items():
    print(k, v)
