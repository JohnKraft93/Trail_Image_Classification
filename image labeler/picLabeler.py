import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
title = tk.Label(text="label picture", width=120)
title.pack()

frame_1 = tk.Frame()
frame_2 = tk.Frame()
frame_3 = tk.Frame()


moterized = tk.Button(
    master=frame_2,
    text="moterized",
    height=7,
    width=20,
    bg = "green",
    fg = "black"
)
moterized.pack(side=tk.LEFT)

nonMoterized = tk.Button(
    master=frame_2,
    text="nonMoterized",
    height=7,
    width=20,
    bg = "green",
    fg = "black"
)
nonMoterized.pack(side=tk.LEFT)

mechanical = tk.Button(
    master=frame_2,
    text="mechanical",
    height=7,
    width=20,
    bg = "green",
    fg = "black"
)
mechanical.pack(side=tk.LEFT)

dog = tk.Button(
    master=frame_2,
    text="dog",
    height=7,
    width=20,
    bg = "green",
    fg = "black"
)
dog.pack(side=tk.LEFT)

junk = tk.Button(
    master=frame_2,
    text="junk",
    height=7,
    width=20,
    bg = "green",
    fg = "black"
)
junk.pack(side=tk.LEFT)

number = tk.Spinbox(master=frame_2, from_=1, to=10, width=20)
number.pack(side=tk.LEFT)

prev = tk.Button(
    master=frame_3,
    text="<-----prev",
    height=7,
    width=60,
    bg = "white",
    fg = "black"
)
prev.pack(side=tk.LEFT)

next_ = tk.Button(
    master=frame_3,
    text="next----->",
    height=7,
    width=60,
    bg = "white",
    fg = "black"
)
next_.pack(side=tk.LEFT)

frame_1.pack()
frame_2.pack()
frame_3.pack()

root.mainloop()