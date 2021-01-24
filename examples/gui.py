import tkinter
class Tkinter:
    def __init__(self):
        self.Tk = None
    class window:
        def create():
            tk.tk = tkinter.Tk()
        def destroy():
            tk.tk.destroy()
        def show():
            tk.tk.mainloop()
    def button(text = "",command = None):
        if command == None:
            c = tkinter.Button(tk.tk,text = text)
        else:
            c = tkinter.Button(tk.tk,text = text,command = command)
        c.pack()
        return c
    def entry():
        c = tkinter.Entry(tk.tk)
        c.pack()
        return c
    def label(text = ""):
        c = tkinter.Label(tk.tk,text = text)
        c.pack()
        return c
    def text():
        c = tkinter.Text(tk.tk)
        c.pack()
        return c
tk = Tkinter
