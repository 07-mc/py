import json,os
bytes = b""
for file in os.listdir("out\\"):
    content = []
    f = open("out\\" + file)
    for c in json.load(f):
        content.append(c)
    bytes += bytearray(content)
    f.close()
with open("file","wb") as file:
    file.write(bytes)