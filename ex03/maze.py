import tkinter as tk


def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20

    elif key == "Down":
        cy += 20
    
    elif key == "Left":
        cx -= 20

    elif key == "Right":
        cx += 20
    
    canvas.coords("kokaton", cx, cy)
    root.after(100 , main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()

    kokaton = tk.PhotoImage(file = "fig/0.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image = kokaton, tag = "kokaton")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()