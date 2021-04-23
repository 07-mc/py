import tkinter,time,sys,re,os,json,tkinter.filedialog,urllib.request,urllib.error
if "examples" not in os.listdir() or not os.path.isdir("examples"):
    os.mkdir("examples")
if "settings.json" not in os.listdir() or not os.path.isfile("settings.json"):
    settings = open("settings.json","w")
    json.dump({"Python path":"python.exe","Tools":True},settings)
    settings.close()
s = open("settings.json")
settings = json.load(s)
s.close()
main = tkinter.Tk()
main.resizable(0,0)
class File():
    def __init__(self):
        self.fn = ""
        if len(sys.argv) >= 2 and os.path.isfile(sys.argv):
            path = ""
            for i in sys.argv[1].split("\\"):
                path = path + i + "/"
            path.rstrip("/")
        self.test = 0
    def open(self):
        fn = tkinter.filedialog.askopenfilename(initialdir='.',title='打开文件',filetypes=("Python代码文件 *.py","Python代码文件 *.pyw"))
        if not fn:
            return
        self.fn = fn
        if not self.fn.endswith(".py") and not self.fn.endswith(".pyw"):
            self.fn += ".py"
        file = open(self.fn,encoding = "utf-8")
        text.delete("0.0","end")
        text.insert("end",file.read())
        file.close()
        main.title("Python代码编辑器 - {}".format(self.fn))
    def save(self):
        if self.fn == "":
            fn = tkinter.filedialog.asksaveasfilename(initialdir='.', title='保存文件', filetypes=("Python代码文件 *.py","Python代码文件 *.pyw"))
            if not fn:
                return
            self.fn = fn
            if not self.fn.endswith(".py") and not self.fn.endswith(".pyw"):
                self.fn += ".py"
            file = open(self.fn,"w",encoding = "utf-8")
            file.write(text.get("0.0","end"))
            file.close()
        else:
            file = open(self.fn,"w",encoding = "utf-8")
            file.write(text.get("0.0","end"))
            file.close()
        os.chdir(re.match("(.*)/{}".format(self.fn.split("/")[-1]),self.fn).group(1))
        main.title("Python代码编辑器 - {}".format(self.fn))
    def reset(self):
        global text
        self.fn = ""
        self.test = 0
        text.delete("0.0","end")
        main.title("Python代码编辑器")
    def run(self):
        self.save()
        if not self.fn:
            return
        self.test += 1
        print(str(self.test) + " ) " + self.fn)
        os.system(settings["Python path"] + " " + self.fn)
        print("\n")
    def show(self):
        os.startfile(".")
f = File()
main.title("Python代码编辑器")
tkinter.Label(main,text = "操作:").pack()
tkinter.Button(main,text = "新建",command = f.reset).pack()
tkinter.Button(main,text = "打开",command = f.open).pack()
tkinter.Button(main,text = "保存",command = f.save).pack()
tkinter.Button(main,text = "运行",command = f.run).pack()
tkinter.Button(main,text = "打开文件夹",command = f.show).pack()
tkinter.Label(main,text = "代码:").pack()
text = tkinter.Text(main)
text.pack()
buttons = []
for file in os.listdir("examples"):
    if os.path.isfile("examples\\" + file) and file.endswith(".py") or file.endswith(".pyw"):
        code = open("examples" + "\\" + file,encoding = "utf-8")
        string = code.read() + "\n"
        code.close()
        class Str():
            def __init__(self,string):
                self.string = string
            def insert(self):
                global text
                text.insert("insert",self.string)
        buttons.append(tkinter.Button(main,text = file.split(".py")[0],command = Str(string).insert))
if buttons != [] and settings["Tools"]:
    tkinter.Label(main,text = "工具:").pack()
    for button in buttons:
        button.pack()
main.mainloop()



