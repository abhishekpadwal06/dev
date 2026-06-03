dog = {"name": "Roscoe", "age": 7}

print(dog["name"])
print(dog['name'])

dog["name"] = "Viola"

print(dog)

print(dog.get("name"))
print(dog.get("colour", "white"))       # Returns default value if it does not exist in the dict

dogCopy = dog.copy()
print(dogCopy)

print(dog.keys())
print(list(dog.keys()))

print(dog.values())
print(list(dog.values()))

dog.pop("name")
print(dog)
dog.popitem()
print(dog)


dog["favourite food"] = "meat"
print(dog)

del dog['favourite food']
print(dog)