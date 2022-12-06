import tkinter as tk
import tkinter.messagebox as tkm

def count_up():
    global tmr, jid
    label["text"] = tmr
    tmr = tmr + 1
    jid = root.after(1000, count_up)

def key_down(event):
    global jid
    if jid is not None:
        root.after_cancel(jid)
        jid = None
    else:
        jid = root.after(1000, count_up)
    key = event.keysym
    tkm.showinfo("キー押下", f"{key}キーが押されました")

if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root, text = "-", font = ("", 80))
    label.pack()

    tmr = 0
    jid = None
    #count_up()
    root.bind("<KeyPress>", key_down)

    root.mainloop()