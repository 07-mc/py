import urllib.request,urllib.parse,string
user = input("user: ").strip()
repo = input("repo: ").strip()
branch = input("branch: ").strip()
if not branch:
    branch = "main"
if branch == "master":
    branch = "main"
url = urllib.parse.quote("https://github.com/{}/{}/archive/{}.zip".format(user,repo,branch),safe=string.printable)
bytes = urllib.request.urlopen(url).read()
with open("{}.{}.{}.zip".format(user,repo,branch),"wb") as f:
    f.write(bytes)
print("Done!")
while True:
    pass