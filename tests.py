import json,os
h = input("h: ")
with open (h,encoding = "utf-8") as f:
    text = f.read()
tests = text.split("编程题")[0]
a = []
for t in tests.split("\n\n"):
    print(t + "\n")
    answer = input("")
    a.append(answer)
with open("选择题答案.json","w") as f:
    json.dump(a,f)
