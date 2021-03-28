import requests,shutil,re,json,sys,os
args = sys.argv
del sys.argv[0]
for arg in args:
    if arg.startswith("vids="):
        vids = re.match("vids=(.*)",arg).group(1)
try:
    vids
except NameError:
    vids = input("vids: ")
if "videos" not in os.listdir():
    os.mkdir("videos")
else:
    if os.path.isfile("videos"):
        os.remove("videos")
    else:
        shutil.rmtree("videos")
        os.mkdir("videos")
with open("{}.txt".format(vids),encoding = "gbk") as f:
    for vid in f.readlines():
        info = [vid.rstrip().split(":")[0],vid.rstrip().split(":")[1]]
        vid = info[1]
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        api_url = 'http://vv.video.qq.com/getinfo?vids=' + vid + '&platform=101001&charge=0&otype=json&defn=shd'
        html = requests.get(api_url, headers=headers).text
        p = re.compile(r'({.*})', re.S)
        jsonstr = re.findall(p, html)[0]
        json_data = json.loads(jsonstr)
        baseurl = json_data['vl']['vi'][0]['ul']['ui'][0]['url']
        fn = json_data['vl']['vi'][0]['fn']
        fvkey = json_data['vl']['vi'][0]['fvkey']
        real_url = baseurl + fn + '?vkey=' + fvkey
        print("{}:\n{} ".format(info[0],real_url))
        res = requests.get(real_url)
        if res.status_code == 200:
            with open("videos\\{}.mp4".format(info[0]),"wb") as f:
                f.write(res.content)
        else:
            print("{}.mp4：下载失败！".format(info[0]))
print("下载完成！")
while True:
    pass