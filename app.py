# Import module
from tkinter import *
import tkinter.font as tkFont
import time
import sys

close = False

times = {}
try:
    with open("user_configuration.conf") as file:
        for line in file:
            if "time" in line:
                hhmmss = line.split()[1].split(":")
                seconds = int(hhmmss[0]) * 60 * 60 + int(hhmmss[1]) * 60 + int(hhmmss[2])
                times[line.split()[0]] = seconds
except:
    pass
sit_time = times.get("sit_time", None) or 2700
stand_time = times.get("stand_time", None) or 900
snooze_time = times.get("snooze_time", None) or 1200


def sit_stand_window(what_window):
    # så programmet stopper hvis man trykker på exit
    global close
    close = True
    # Create object
    root = Tk()
    root.iconbitmap('res/chair.ico')
    root.title('Stand up reminder')
    root.attributes('-topmost', 'true')

    # Adjust size
    root.geometry("500x299")
    fontStyle = tkFont.Font(family="Arial", size=18)
    # Add image file
    bg = PhotoImage(file=f"res/{what_window}.png")

    # Show image using label
    label1 = Label(root, image=bg)
    label1.place(x=0, y=0)
    adjustx = -20
    # Add buttons
    if (what_window == "start"):
        button1 = Button(root, text=f"Awesome! \o/ see you in {int(sit_time/60)} minutes", bg="#3DB93B", font=fontStyle,
                         command=lambda: close_window(root))
        button1.pack(pady=20)
        button1.place(x=50 + adjustx, y=200)

        button2 = Button(root, text="Nevermind (¬_¬ )", bg="#3DB93B", font=fontStyle,
                         command=lambda: close_program(root))
        button2.pack(pady=20)
        button2.place(x=150 + adjustx, y=250)

    elif (what_window == "stand"):
        button1 = Button(root, text="I'm standing! \o/", bg="#3DB93B", font=fontStyle,
                         command=lambda: close_window(root))
        button1.pack(pady=20)
        button1.place(x=50 + adjustx, y=200)

        button2 = Button(root, text="snooze... (￣o￣) . z Z", bg="#3DB93B", font=fontStyle,
                         command=lambda: snooze_window(root, what_window))
        button2.pack(pady=20)
        button2.place(x=250 + adjustx, y=200)

        button3 = Button(root, text="disable for today (∪.∪ )...zzz", bg="#3DB93B", font=fontStyle,
                         command=lambda: close_program(root))
        button3.pack(pady=20)
        button3.place(x=100 + adjustx, y=250)
    elif (what_window == "sit"):
        button1 = Button(root, text="I'm sitting b(￣▽￣)d", bg="#3DB93B", font=fontStyle,
                         command=lambda: close_window(root))
        button1.pack(pady=20)
        button1.place(x=25 + adjustx, y=200)

        button2 = Button(root, text="snooze! o((>ω< ))o", bg="#3DB93B", font=fontStyle,
                         command=lambda: snooze_window(root, what_window))
        button2.pack(pady=20)
        button2.place(x=275 + adjustx, y=200)

        button3 = Button(root, text="disable for today (╯°□°）╯︵ I┻", bg="#3DB93B",
                         command=lambda: close_program(root))
        button3.pack(pady=20)
        button3.place(x=100 + adjustx, y=250)

    # Execute tkinter
    root.resizable(False, False)
    root.mainloop()


def close_program(window_root):
    window_root.destroy()


def close_window(window_root):
    global close
    close = False
    window_root.destroy()


def snooze_window(window_root, what_window):
    window_root.destroy()
    time.sleep(snooze_time)
    sit_stand_window(what_window)


def loop():
    sit_stand_window("start")
    while not close:
        if (not "start_fast" in sys.argv):
            time.sleep(sit_time)
        sit_stand_window("stand")
        if close:
            return
        time.sleep(stand_time)
        sit_stand_window("sit")
        if close:
            return


loop()
