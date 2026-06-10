import tkinter as tk
import random

def start_game():
    global n, correct, score, total_questions
    name = entry_name.get()
    level = difficulty.get()
    total_questions = question_count.get()
    score = 0

    if level == "かんたん":
        low, high = 2, 50
    elif level == "ふつう":
        low, high = 51, 100
    else:
        low, high = 101, 500

    n = random.randint(low, high)
    correct = prime_factors(n)

    frame_start.pack_forget()
    frame_game.pack()
    _root.bind("<Return>",lambda event: check_answer())
    
    #ゲーム画面のラベルを更新
    lbl_question.config(text= f"{n}を素因数分解してください\n(カンマ区切りで入力)\n(例：18の場合2,3,3)")
    lbl_score.config(text=f"{name}さん 0/{total_questions}")

#素因数分解の関数
def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
            pass
        else:
            i = i + 1
            pass
    return factors

#正誤判定の関数
def check_answer(): 
    global n, correct, score #global宣言
    answer = entry_answer.get() #入力欄の文字を取得
    if answer == "":
        return
    result = [int(x) for x in answer.split(",")]

    if sorted(result) == sorted(correct):
        lbl_result.config(text="正解！", fg="green")
        
        if difficulty.get() == "かんたん":
            low, high = 2, 50
        elif difficulty.get()  == "ふつう":
            low, high = 51, 100
        else:
            low, high = 101, 500
        n = random.randint(low, high)

        correct = prime_factors(n)

        lbl_question.config(text= f"{n}を素因数分解してください\n(カンマ区切りで入力)\n(例：18の場合2,3,3)")
        entry_answer.delete(0, tk.END) #入力欄を空にする
        score += 1
        lbl_score.config(text= f"{entry_name.get()}さん{score}/{total_questions}")

        if score >= total_questions:
            #終了画面を表示
            frame_game.pack_forget()
            lbl_finish.config(text= f"ゲーム終了！\n{entry_name.get()}さん{total_questions}問中{score}問正解！")
            frame_finish.pack()
        

    else:
        lbl_result.config(text=f"残念...正解は{correct}でした", fg= "red")

#ヒントを出す関数
def show_hint():
    lbl_result.config(text= f"ヒント：最小の素因数は{correct[0]}です", fg= "blue")

def replay():
    global score
    frame_finish.pack_forget()
    frame_game.pack()
    lbl_result.config(text="")
    start_game()

def back_to_start():
    frame_finish.pack_forget()
    frame_start.pack()
    lbl_result.config(text="")
    _root.bind("<Return>", lambda event: start_game())



###################### UI ######################


#ゲーム画面
def build(root, frame, back_to_top= None):
    global frame_start, frame_game, frame_finish
    global lbl_question, lbl_result, lbl_score, lbl_question, lbl_answer, lbl_finish
    global entry_name, question_count, entry_answer
    global score, total_questions, difficulty, n
    global _root
    _root = root

    frame_start = tk.Frame(frame)
    frame_start.pack()

    frame_game = tk.Frame(frame)

    tk.Label(frame_start, text= "===素因数分解ゲーム===", font=("Arial", 20)).pack(pady=20)
    tk.Label(frame_start, text= "名前を入力してください", font=("Arial", 12)).pack()
    entry_name = tk.Entry(frame_start, font=("Arial", 12))
    entry_name.pack(pady=5)

    #難易度ラジオボタン
    tk.Label(frame_start, text="難易度を選んでください", font=("Arial", 12)).pack(pady=5)
    difficulty = tk.StringVar(value="かんたん")
    for level in ["かんたん", "ふつう", "むずかしい"]:
        tk.Radiobutton(frame_start, text= level, variable = difficulty, value= level, font=("Arial", 12)).pack()

    #問題数ラジオボタン
    tk.Label(frame_start, text="問題数を選んでください", font=("Arial", 12)).pack(pady=12)
    question_count = tk.IntVar(value=3)
    for count in(3, 5, 10):
        tk.Radiobutton(frame_start, text= f"{count}問", variable= question_count, value= count, font=("Arial",12)).pack()

    tk.Button(frame_start, text="スタート", font=("Arial", 14), command= start_game).pack(pady=20)


    #スコアラベル
    lbl_score = tk.Label(frame_game, text= "スコア：0", font=("Arial", 12))
    lbl_score.pack()

    #問題文ラベル
    lbl_question = tk.Label(frame_game, text= "", font=("Arial", 14))
    lbl_question.pack(pady=10)

    #入力欄
    entry_answer = tk.Entry(frame_game, font=("Arial", 14), width= 20)
    entry_answer.pack(pady=10)

    #決定ボタン
    btn_submit = tk.Button(frame_game, text="決定", font=("Arial", 12), command=check_answer)
    btn_submit.pack(pady=10)

    #ヒントボタン
    btn_hint = tk.Button(frame_game, text="ヒント", font=("Arial", 12), command= show_hint)
    btn_hint.pack(pady= 5)

    #結果表示ラベル
    lbl_result = tk.Label(frame_game, text="", font=("Arial", 14))
    lbl_result.pack(pady=10)

    #結果表示後のアクション
    frame_finish = tk.Frame(frame)
    lbl_finish = tk.Label(frame_finish, text= "", font=("Arial", 16))
    lbl_finish.pack(pady=40)
    tk.Button(frame_finish, text="もう一度遊ぶ", font=("Arial", 12), command= replay).pack(pady=10)
    tk.Button(frame_finish, text="素因数分解ゲームスタート画面へ戻る", font=("Arial", 12), command= back_to_start).pack(pady=10)
    if back_to_top:
        tk.Button(frame_finish, text= "ゲーム選択に戻る", font=("Arial", 12), command=back_to_top).pack(pady=10)
 

#UI
if __name__ == "__main__":

    root = tk.Tk()
    root.title("素因数分解ゲーム")
    root.geometry("600x600")
    frame = tk.Frame(root)
    frame.pack()
    build(root,frame)
    root.mainloop()