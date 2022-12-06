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

    elif key == "Down":
        my += 1
    
    elif key == "Left":
        mx -= 1

    elif key == "Right":
        mx += 1

    if maze_lst[mx][my] == 1:
        #kokaton = tk.PhotoImage(file = "fig/7.png")
        #canvas.create_image(cx, cy, image = kokaton, tag = "kokaton") #こうかとんの表示
        if key == "Up":
            my += 1

        elif key == "Down":
            my -= 1
        
        elif key == "Left":
            mx += 1

        elif key == "Right":
            mx -= 1

    if (cx == tx and cy == ty) or (cx == tx2 and cy == ty2): #敵と接触したら
        mx = 1
        my = 1
        tkm.showinfo("警告", f"Crush!")
    if cx == gx and cy == gy:
        mx, my = 1, 1
        tkm.showinfo("Goal", f"Congratulations!")
    cx, cy = mx*100 + 50, my*100 + 50
            
    canvas.coords("kokaton", cx, cy)
    
    root.after(100, main_proc)

def karasu_proc(): #敵をランダムに動かす関数
    global kx, ky, tx, ty, kx2, ky2, tx2, ty2
    rd = randint(0, 3)
    if rd == 0:
        ky -= 1
        kx2 -= 1

    elif rd == 1:
        ky += 1
        ky2 += 1
    
    elif rd == 2:
        kx -= 1
        ky2 -= 1

    elif rd == 3:
        kx += 1
        kx2 += 1

    if maze_lst[kx][ky] == 1:
        if rd == 0:
            ky += 1

        elif rd == 1:
            ky -= 1
        
        elif rd == 2:
            kx += 1

        elif rd == 3:
            kx -= 1

    if maze_lst[kx2][ky2] == 1:
        if rd == 0:
            kx2 += 1

        elif rd == 1:
            ky2 -= 1
        
        elif rd == 2:
            ky2 += 1

        elif rd == 3:
            kx2 -= 1
    tx, ty = kx*100 + 50, ky*100 + 50
    tx2, ty2 = kx2*100 + 50, ky2*100 + 50
    canvas.coords("karasu", tx, ty)
    canvas.coords("karasu2", tx2, ty2)
    
    root.after(100, karasu_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #タイトル
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black") #キャンバスの生成
    canvas.pack()
    
    maze_lst = mm.make_maze(15, 9) #迷路の生成
    mm.show_maze(canvas, maze_lst) #迷路の表示

    kokaton = tk.PhotoImage(file = "fig/0.png") #画像の読み込み
    mx, my = 1, 1 #こうかとんの初期位置
    cx, cy = mx*100 + 50, my*100 + 50 #こうかとんの初期位置
    start = tk.PhotoImage(file = "s.png") #スタート地点
    sx, sy = 1*100+50, 1*100+50 #スタート地点の座標
    goal = tk.PhotoImage(file = "G.png") #ゴール地点
    kx, ky = 10, 6 #敵の初期位置
    kx2, ky2 = 1, 4
    tx, ty = kx*100 + 50, ky*100 + 50
    tx2, ty2 = kx2*100 + 50, ky2*100 + 50
    gx, gy = 13*100+50, 7*100+50 #ゴールの座標
    karasu = tk.PhotoImage(file = "karasu.png") #敵の座標の読み込み
    canvas.create_image(sx, sy, image = start) #スタートの表示
    canvas.create_image(gx, gy, image = goal) #ゴールの表示
    canvas.create_image(tx, ty, image = karasu, tag = "karasu") #敵の表示
    canvas.create_image(tx2, ty2, image = karasu, tag = "karasu2") #敵の表示
    canvas.create_image(cx, cy, image = kokaton, tag = "kokaton") #こうかとんの表示
    
    key = "" #キーの初期化
    root.bind("<KeyPress>", key_down) #関数の呼び出し
    root.bind("<KeyRelease>", key_up)
    
    karasu_proc()
    main_proc() #関数の呼び出し
    root.mainloop()