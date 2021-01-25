import json,os,shutil
if "out" in os.listdir():
    shutil.rmtree("out")
os.mkdir("out")
file = input("file: ")
list = []
num = 1
with open(file, "rb") as f1:
    for byte in f1.read():
        list.append(byte)
for n in range(0,len(list),5000000):
    f2 = open("out\\out" + str(num) + ".json","w")
    json.dump(list[5000000 * num - 5000000 : 5000000 * num],f2)
    f2.close()
    num += 1
