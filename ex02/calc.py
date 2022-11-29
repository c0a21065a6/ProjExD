import tkinter as tk
import tkinter.messagebox as tkm

# 練習３
def button_click(event):
    btn = event.widget
    num = btn["text"]
    #練習7
    if num == "=" or num == "%" or num == "√":
        siki = entry.get() #数式の文字列
        for i in range(len(siki)): #"×","÷"を"*","/"に換える
            if siki[i] == "×":
                siki = siki[0:i] + "*" + siki[i + 1:]
            elif siki[i] == "÷":
                siki = siki[0:i] + "/" + siki[i + 1:]
                
            #print(siki[i])
        try:
            res = eval(siki)
            entry.delete(0, tk.END)
            if num == "%": #"%"ボタンの実装
                res = res/100
            
            elif num == "√": #"√"ボタンの実装
                res = res ** (1/2)

            entry.insert(tk.END, res)
        
        except:
            tkm.showinfo("", f"無効な式が入力されました") #無効な式が入力され場合の処理
    
    elif num == "AC": #AllClearボタンの実装
        entry.delete(0, tk.END)
    
    

    else:
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
        #練習6
        entry.insert(tk.END, num)

# 練習１
root = tk.Tk()
root.geometry("400x700")

#練習4
entry = tk.Entry(root, justify = "right", width = 10, font = ("", 40))
entry.grid(row = 0, column = 0, columnspan = 3)

# 練習２
r, c = 2, 2
for num in range(9, -1, -1): #数字ボタンの作成
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
    if num == 0:
        c = 1
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c -= 1
    if c < 0:
        r += 1
        c = 2

#練習5
#四則演算ボタンの作成
r = 1
c = 3
operators = ["+", "-", "×", "÷", "="] 
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    r += 1
    if r == 6:
        r -= 1
        c -= 1
        if r == 5 and c == 2:
            c -= 1

#各種ボタンの作成
r = 1
c = 0
other = ["%", ".", "√"] 
for oth in other:
    button = tk.Button(root, text=f"{oth}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c == 3:
        r += 1
        c = 0

#オールクリアボタンの作成
button = tk.Button(root, text=f"AC", width=4, height=2, font=("", 30))
button.grid(row=0, column=3)
button.bind("<1>", button_click)

#括弧ボタンの作成
r = 5
c = 0
kakko = ["(", ")"]
for ka in kakko:
    button = tk.Button(root, text=f"{ka}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 2


root.mainloop()