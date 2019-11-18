# 名字 -> 字典名稱[名字]
person = {
    "name":"Elwing",
    "height":175,
    "over18":True
}
# print(name)
print(person["name"])
# weight = 75
person["weight"] = 75
print(person)
# height = 180
person["height"] = 180
print(person)
# weight = weight + 5
person["weight"] = person["weight"] + 5
print(person)
# del
del person["over18"]
print(person)

for key in person:
    print(key, person[key])