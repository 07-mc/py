import json
file = input("file: ")
list = []
with open(file, "rb") as f:
    for byte in f.read():
        list.append(byte)
with open("out.json", "w") as out:
    json.dump(list, out)