import tkinter as tk
import re
import random
from itertools import permutations, product

#スタート画面
def start_game():
    global n, correct, score, total_questions, numbers,name, current_q
    name = entry_name.get()
    total_questions = question_count.get()
    score = 0
    current_q = 0
    while True:
        numbers = random.sample(range(1, 10), 4)
        if can_make_10(numbers):
            break
    frame_start.pack_forget()
    frame_game.pack()
    _root.bind("<Return>", lambda event: check_answer())
    entry_answer.delete(0, tk.END)
    lbl_score.config(text= f"{name}さん{score}/{total_questions}")

    #ゲーム画面のラベルを更新
    lbl_question.config(text= f"{numbers}この4つの数字を使って四則演算で10を作ってください\n(例：[2,3,4,5]の場合、2*4-3+5)")
    lbl_score.config(text=f"{name}さん0/{total_questions}")
    entry_answer.delete(0, tk.END)

#遊び方の画面へ行く関数
def go_how_to():
    frame_start.pack_forget()
    frame_how_to.pack()

#遊び方の画面からスタート画面に行く関数
def back_to_start_from_how_to():
    frame_how_to.pack_forget()
    frame_start.pack()

ops = ["+", "-", "*", "/"]

#4つの数字と3つの演算子で10が作れるかを判定する関数
def can_make_10(numbers):
    #数字の並べ方をすべて試す
    for nums in permutations(numbers):
        #演算子の組み合わせをすべて試す(3つの演算子が必要)
        for op_combo in product(ops, repeat=3):
            expression = f"{nums[0]}{op_combo[0]}{nums[1]}{op_combo[1]}{nums[2]}{op_combo[2]}{nums[3]}"
            #ここで計算して10になるかチェック
            try:
                if eval(expression) == 10:
                    return True
            except ZeroDivisionError:
                pass
    return False


#正誤判定の関数
def check_answer():
    global score, numbers,name, current_q
    current_q += 1
    expression = entry_answer.get()
    used_numbers = [int(x) for x in re.findall(r'\d',expression)]
    try:
        result = eval(expression)

        if result == 10 and sorted(used_numbers) == sorted(numbers):
            lbl_result.config(text="正解！")
            score += 1
        else:
            solution = get_solution(numbers)
            lbl_result.config(text= f"不正解 解答例：{solution}")
    except:
        lbl_result.config(text="式が正しくありません")
        return

    #次の問題へ
    while True:
        numbers = random.sample(range(1, 10), 4)
        if can_make_10(numbers):
            break
    lbl_question.config(text= f"{numbers}この4つの数字を使って四則演算で10を作ってください\n(例：[2, 3, 4, 5]の場合、2*4-3+5)")
    entry_answer.delete(0, tk.END)
    lbl_score.config(text= f"{name}さん{score}/{total_questions}")

    if current_q >= total_questions:
        frame_game.pack_forget()
        frame_finish.pack()
        lbl_finish.config(text= f"{name}さんの結果：{score}問中{total_questions}問正解！")

#正解例を渡す関数
def get_solution(numbers):
    #数字の並べ方をすべて試す
    for nums in permutations(numbers):
        #演算子の組み合わせをすべて試す(3つの演算子が必要)
        for op_combo in product(ops, repeat=3):
            expression = f"{nums[0]}{op_combo[0]}{nums[1]}{op_combo[1]}{nums[2]}{op_combo[2]}{nums[3]}"
            #ここで計算して10になるかチェック
            try:
                if eval(expression) == 10:
                    return expression
            except ZeroDivisionError:
                pass
    return False

###################### UI ######################

#ゲーム画面
def build(root, frame, back_to_top= None):
    global frame_start, frame_game, frame_finish, frame_how_to
    global lbl_question, lbl_result, lbl_score, lbl_question, lbl_answer, lbl_finish
    global entry_name, question_count, entry_answer
    global score, total_questions, n
    global _root
    _root = root

    #スタート画面に戻る
    def back_to_start():
        frame_finish.pack_forget()
        frame_start.pack()

    frame_start = tk.Frame(frame)
    frame_start.pack()

    frame_game = tk.Frame(frame)

    #タイトルのラベル
    tk.Label(frame_start, text= "===Make10パズル===", font=("Arial", 20)).pack(pady=20)
    tk.Label(frame_start, text= "名前を入力してください",font=("Arial",12)).pack()
    entry_name = tk.Entry(frame_start, font=("Arial", 12))
    entry_name.pack(pady=5)

    #問題数ラジオボタン
    tk.Label(frame_start, text= "問題数を選んでください", font=("Arial", 12)).pack(pady=12)
    question_count = tk.IntVar(value=3)
    for count in(3, 5, 10):
        tk.Radiobutton(frame_start, text= f"{count}問", variable= question_count, value= count, font=("Arial", 12)).pack()
    
    tk.Button(frame_start, text= "スタート", font=("Arial", 14), command= start_game).pack(pady=20)
    
    #遊び方の説明ページへのボタン
    frame_how_to = tk.Frame(frame)
    tk.Button(frame_start, text= "遊び方", font=("Arial", 14), command=go_how_to).pack(pady=10)
    
    #遊び方の説明
    tk.Label(frame_how_to, text="遊び方", font=("Arial", 18)).pack(pady=20)
    tk.Label(frame_how_to, text="make10パズルのルール\n1～9までの数字が4つランダムに生成されます。\nその4つの数字と四則演算を使って10を作ってください。\n使用可能な記号：+ - * / ()\n例：[2, 3, 4, 5]\nあなたの回答例：2*4-3+5", font=("Arial", 12)).pack(pady=20)
    tk.Button(frame_how_to, text="スタート画面に戻る", font=("Arial", 12), command= back_to_start_from_how_to).pack(pady=10)
    
    #スコアラベル
    lbl_score = tk.Label(frame_game, text= "スコア：0", font=("Arial", 12))
    lbl_score.pack()

    #問題
    lbl_question = tk.Label(frame_game, text="", font=("Arial", 12))
    lbl_question.pack(pady=10)

    #入力欄
    entry_answer = tk.Entry(frame_game, font=("Arial", 14))
    entry_answer.pack(pady=10)

    #決定ボタン
    btn_submit = tk.Button(frame_game, text="決定", font=("Arial", 12),command= check_answer)
    btn_submit.pack(pady=10)

    #正誤ラベル
    lbl_result = tk.Label(frame_game, text= "", font=("Arial", 12))
    lbl_result.pack()


    #結果表示後のアクション
    frame_finish = tk.Frame(frame)
    lbl_finish = tk.Label(frame_finish, text= "", font=("Arial", 16))
    lbl_finish.pack(pady=40)
    tk.Button(frame_finish, text="もう一度遊ぶ", font=("Arial", 12), command= back_to_start).pack(pady=10)
    if back_to_top:
        def go_top():
            frame_finish.pack_forget()
            back_to_top()
        tk.Button(frame_finish, text= "トップに戻る", font=("Arial", 12), command= go_top).pack(pady=10)


    #UI
if __name__ == "__main__":

    root = tk.Tk()
    root.title("Make10パズル")
    root.geometry("600x600")
    frame = tk.Frame(root)
    frame.pack()
    build(root, frame)
    root.mainloop()