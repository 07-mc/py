import json
json_file = open("字典.json",encoding = "utf-8")
字典 = json_file.read()
json_file.close()
while True:
    i = input(">>>")
    if i:
        for 拼音 in i.split():
            for 汉字的拼音 in 字典[拼音[0]].keys():
                if 汉字的拼音 == 拼音:
                    print(汉字的拼音,字典[拼音[0]][汉字的拼音])
