import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
from random import randint
def key_down(event):#キーが押された際の関数
    global key
    key = event.keysym

def key_up(event):#キーが離された際の関数
    global key
    key = ""

def main_proc():#こうかとんの挙動
    global cx, cy, mx, my
    if key == "Up":
        my -= 1

    if key == "Down":
        my += 1
    
    if key == "Left":
        mx -= 1

    if key == "Right":
        mx += 1

    if maze_lst[mx][my] == 1:
        #kokaton = tk.PhotoImage(file = "fig/7.png")
        #canvas.create_image(cx, cy, image = kokaton, tag = "kokaton") #こうかとんの表示
        if key == "Up":
            my += 1

        if key == "Down":
            my -= 1
        
        if key == "Left":
            mx += 1

        if key == "Right":
            mx -= 1

    if cx == tx and cy == ty:
        mx = 1
        my = 1
        tkm.showinfo("警告", f"Crush!")
    cx, cy = mx*100 + 50, my*100 + 50
    
        
    canvas.coords("kokaton", cx, cy)
    if cx == gx and cy == gy:
        tkm.showinfo("Goal", f"Congratulations!")
    root.after(100, main_proc)

def karasu_proc():
    global kx, ky, tx, ty
    rd = randint(0, 3)
    if rd == 0:
        ky -= 1

    if rd == 1:
        ky += 1
    
    if rd == 2:
        kx -= 1

    if rd == 3:
        kx += 1

    if maze_lst[kx][ky] == 1:
        if rd == 0:
            ky += 1

        if rd == 1:
            ky -= 1
        
        if rd == 2:
            kx += 1

        if rd == 3:
            kx -= 1

    tx, ty = kx*100 + 50, ky*100 + 50
    canvas.coords("karasu", tx, ty)
    
    root.after(100, karasu_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #タイトル
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black") #キャンバスの生成
    canvas.pack()
    
    maze_lst = mm.make_maze(15, 9) #迷路の生成
    #mm.print_maze(maze_lst)
    mm.show_maze(canvas, maze_lst) #迷路の表示

    kokaton = tk.PhotoImage(file = "fig/0.png") #画像の読み込み
    mx, my = 1, 1 #こうかとんの初期位置
    cx, cy = mx*100 + 50, my*100 + 50 #こうかとんの初期位置
    start = tk.PhotoImage(file = "s.png")
    sx, sy = 1*100+50, 1*100+50
    goal = tk.PhotoImage(file = "G.png")
    kx, ky = 6, 6
    tx, ty = kx*100 + 50, ky*100 + 50
    gx, gy = 13*100+50, 7*100+50
    karasu = tk.PhotoImage(file = "karasu.png")
    canvas.create_image(sx, sy, image = start) #スタートの表示
    canvas.create_image(gx, gy, image = goal) #ゴールの表示
    canvas.create_image(tx, ty, image = karasu, tag = "karasu") #敵の表示
    canvas.create_image(cx, cy, image = kokaton, tag = "kokaton") #こうかとんの表示
    
    key = "" #キーの初期化
    root.bind("<KeyPress>", key_down) #関数の呼び出し
    root.bind("<KeyRelease>", key_up)
    
    karasu_proc()
    main_proc() #関数の呼び出し
    root.mainloop()