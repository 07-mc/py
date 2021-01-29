import json
json_file = open("字典.json",encoding = "utf-8")
字典 = json.load(json_file)
json_file.close()
while True:
    i = input(">>>").lower()
    if i:
        for 拼音 in i.split():
            find = False
            if 拼音[0] in 字典.keys():
                for 汉字的拼音 in 字典[拼音[0]].keys():
                    if 汉字的拼音 == 拼音:
                        print(汉字的拼音,字典[拼音[0]][汉字的拼音])
                        find = True
                if not find:
                    print("# 没有找到 - “" + 拼音 + "”")
            else:
                print("# 没有找到 - “" + 拼音 + "“")