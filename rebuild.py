import json
with open("out.json") as bytes:
    list = json.load(bytes)
with open("output", "wb") as f:
    f.write(bytearray(list))
