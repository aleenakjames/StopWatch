from tkinter import *
import sys
import time

global count
count = 0


class stopwatch():
    def reset(self):
        global count
        count = 1
        self.pause['state'] = 'disabled'
        self.start['state'] = 'normal'
        self.resume['state'] = 'disabled'
        self.reset['state'] = 'disabled'
        self.t.set('00:00:00')

    def start(self):
        global count
        count = 0
        self.start['state'] = 'disabled'
        self.resume['state'] = 'disabled'
        self.pause['state'] = 'normal'
        self.reset['state'] = 'disabled'
        self.timer()

    def pause(self):
        global count
        count = 1
        self.start['state'] = 'disabled'
        self.resume['state'] = 'normal'
        self.pause['state'] = 'disable'
        self.reset['state'] = 'normal'

    def resume(self):
        global count
        count = 0
        self.start['state'] = 'disabled'
        self.resume['state'] = 'disable'
        self.pause['state'] = 'normal'
        self.reset['state'] = 'disabled'
        self.timer()

    def timer(self):
        global count
        if count == 0:
            self.d = str(self.t.get())
            h, m, s = map(int, self.d.split(":"))
            h = int(h)
            m = int(m)
            s = int(s)
            if s < 59:
                s += 1
            elif s == 59:
                s = 0
                if m < 59:
                    m += 1
                elif m == 59:
                    m = 0
                    h += 1
            if h < 10:
                h = str(0) + str(h)
            else:
                h = str(h)
            if m < 10:
                m = str(0) + str(m)
            else:
                m = str(m)
            if s < 10:
                s = str(0) + str(s)
            else:
                s = str(s)
            self.d = h + ":" + m + ":" + s
            self.t.set(self.d)
            if count == 0:
                self.root.after(1000, self.timer)

    def __init__(self):
        self.root = Tk()
        self.root.title("Stop Watch")
        self.root.geometry("600x200")
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root, textvariable=self.t, font=("Times 40 bold"), bg="#90FF92")
        self.start = Button(self.root, text="Start", command=self.start, font=("Times 12 bold"), bg=("#F8FFED"))
        self.pause = Button(self.root, text="Pause", command=self.pause, font=("Times 12 bold"), bg=("#F8FFED"))
        self.resume = Button(self.root, text="Resume", command=self.resume, font=("Times 12 bold"), bg=("#F8FFED"))
        self.reset = Button(self.root, text="Reset", command=self.reset, font=("Times 12 bold"), bg=("#F8FFED"))
        self.lb.place(x=160, y=10)
        self.start.place(x=120, y=100)
        self.pause.place(x=220, y=100)
        self.resume.place(x=320, y=100)
        self.reset.place(x=420, y=100)
        self.label = Label(self.root, text="", font=("Times 40 bold"))
        self.root.configure(bg='#90FF92')
        self.root.mainloop()


a = stopwatch()
