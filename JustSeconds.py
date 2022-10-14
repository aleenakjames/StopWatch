import tkinter as tk

count = -1
run = False


def var_name(mark):
    def value():
        if run:
            global count
            # Just beore starting
            if count == -1:
                show = "Starting"
            else:
                show = str(count)
            mark['text'] = show
            # Increment the count after
            # every 1 second
            mark.after(1000, value)
            count += 1

    value()


# While Running
def Start(mark):
    global run
    run = True
    var_name(mark)
    start['state'] = 'disabled'
    pause['state'] = 'normal'
    reset['state'] = 'disabled'


# While stopped
def Stop():
    global run
    start['state'] = 'disabled'
    pause['state'] = 'disabled'
    reset['state'] = 'normal'
    resume['state'] = 'normal'
    run = False


# To resume
def Resume(mark):
    global run
    run = True
    var_name(mark)
    resume['state'] = 'disabled'
    start['state'] = 'disabled'
    pause['state'] = 'normal'
    reset['state'] = 'disabled'


# For Reset
def Reset(mark):
    global count
    count = -1
    if run == False:
        reset['state'] = 'disabled'
        mark['text'] = 'Welcome'
        start['state'] = 'normal'
        resume['state'] = 'disabled'
    else:
        mark['text'] = 'Start'


base = tk.Tk()
base.title("PYTHON STOPWATCH")
base.minsize(width=300, height=200)
mark = tk.Label(base, text="Welcome", fg="blue", font="Times 25 bold", bg="white")
mark.pack()
start = tk.Button(base, text='Start', width=25, command=lambda: Start(mark))
pause = tk.Button(base, text='Pause', width=25, state='disabled', command=Stop)
reset = tk.Button(base, text='Reset', width=25, state='disabled', command=lambda: Reset(mark))
resume = tk.Button(base, text='Resume', width=25, state='disabled', command=lambda: Resume(mark))
start.pack()
pause.pack()
resume.pack()
reset.pack()
base.mainloop()
