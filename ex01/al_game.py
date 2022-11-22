import random
import time
num_of_alphabet = 26
num_of_all_chars = 10
num_of_abs_chars = 3
num_of_trials = 2

def shutudai(alphabet):
    all_chars = random.sample(alphabet, num_of_all_chars)
    print("対象文字:")
    for c in all_chars:
        print(c, end = " ")
    print()

    abs_chars = random.sample(all_chars, num_of_abs_chars)
    #print("欠損文字（デバッグ用）:")
    #for c in abs_chars:
    #    print(c, end = " ")
    #print()

    print("表示文字:")
    for c in all_chars:
        if c not in abs_chars:
            print(c, end = "")
    print()

    return abs_chars

def kaitou(abs_chars):
    num = int(input("欠損文字はいくつあるでしょうか？"))
    if num != num_of_abs_chars:
        print("不正解です。")

    else:
        print("正解です。具体的に欠損文字を入力してください")
        for i in range(num):
            ans = input(f"{i+1}つ目の文字を入力してください：")
            if ans not in abs_chars:
                print("不正解です。")
                return False
            else:
                abs_chars.remove(ans)
        print("全問正解です。")
        return True

if __name__ == "__main__":
    st = time.time()
    alphabet = [chr(i + 65) for i in range(num_of_alphabet)]
    print(alphabet)
    for _ in range(num_of_trials):
        abs_chars = shutudai(alphabet)
        ret = kaitou(abs_chars)
        if ret:
            break
        else:
            print("-"*20)
    ed = time.time()
    print(f"所要時間:{(ed-st):.02}秒")