import tkinter as tk
import random

#素数判定
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

#正誤判定
def check_prime(user_answer):
    global n, score, total_questions
    if user_answer == is_prime(n):
        lbl_result.config(text="正解！", fg="green")
        score += 1
    else:
        lbl_result.config(text=f"残念...正解は{'素数' if is_prime(n) else '素数でない'}でした", fg="red")

    # 正解不正解に関わらず問題数をカウント
    total_questions -= 1
    lbl_score.config(text=f"{entry_name.get()}さん スコア：{score}")

    if total_questions <= 0:
        frame_prime.pack_forget()
        lbl_finish.config(text=f"ゲーム終了！\n{entry_name.get()}さん {question_count.get()}問中{score}問正解！")
        frame_finish.pack()
    else:
        n = random.randint(2, 50)
        lbl_question.config(text=f"{n}は素数ですか？")

#もう一度遊ぶための関数
def replay():
    global score, n, total_questions
    score = 0
    total_questions = question_count.get()
    n = random.randint(2, 50)
    frame_finish.pack_forget()
    frame_prime.pack()
    lbl_question.config(text=f"{n}は素数ですか？")
    lbl_result.config(text="")
    lbl_score.config(text="スコア：0")

#初期化関連
def start_game():
    global score, total_questions, n
    score = 0
    total_questions = question_count.get()
    n = random.randint(2, 50)
    frame_start.pack_forget()
    frame_prime.pack()
    lbl_question.config(text= f"{n}は素数ですか？")
    lbl_score.config(text= f"{entry_name.get()}さん スコア：0")

#ゲーム終了後内容を初期化する関数
def reset():
    frame_finish.pack_forget()
    frame_prime.pack_forget()
    lbl_result.config(text="")
    frame_start.pack()

#スタート画面に戻る関数
def back_to_start():
    global score, n, total_questions
    score = 0
    frame_finish.pack_forget()
    frame_start.pack()
    lbl_result.config(text="")

#ルートの関数化
def build(root, frame, back_to_top=None):
    global frame_prime, frame_finish, frame_start, entry_name, difficulty, question_count
    global lbl_question, lbl_result, lbl_score, lbl_finish
    global score, total_questions, n

    #スタート画面
    frame_start = tk.Frame(frame)
    frame_start.pack()
    frame_prime = tk.Frame(frame)

    tk.Label(frame_start, text= "===素数判定ゲーム===",font=("Arial", 20)).pack(pady=20)
    tk.Label(frame_start, text= "名前を入力してください", font=("Arial", 12)).pack()
    entry_name = tk.Entry(frame_start, font=("Arial", 12))
    entry_name.pack(pady=5)

    #難易度選択
    tk.Label(frame_start, text="難易度を選んでください", font=("Arial", 12)).pack(pady=12)
    difficulty = tk.StringVar(value="かんたん")
    for level in ["かんたん", "ふつう", "むずかしい"]:
        tk.Radiobutton(frame_start, text= level, variable= difficulty, value= level, font=("Arial", 12)).pack()
    
    tk.Label(frame_start, text="問題数を選んでください", font=("Arial", 12)).pack(pady=12)
    question_count = tk.IntVar(value=3)
    for count in (3, 5, 10):
        tk.Radiobutton(frame_start, text= f"{count}問", variable= question_count, value= count, font=("Arial", 12)).pack()
    
    tk.Button(frame_start, text= "スタート", font=("Arial", 14), command= start_game).pack(pady=20)
    root.bind("<Return>", lambda event: start_game())
    
    #問題文ラベル
    lbl_question = tk.Label(frame_prime, text="", font=("Arial", 14))
    lbl_question.pack(pady=20)

    #素数ボタン
    btn_prime = tk.Button(frame_prime, text="素数", font=("Arial", 14), command=lambda: check_prime(True))
    btn_prime.pack(side="left", padx=20)

    #素数ではないボタン
    btn_not_prime = tk.Button(frame_prime, text="素数でない", font=("Arial", 14), command=lambda: check_prime(False))
    btn_not_prime.pack(side="left", padx=20)

    #結果表示ラベル
    lbl_result = tk.Label(frame_prime, text="", font=("Arial", 16))
    lbl_result.pack(pady=10)

    #スコア表示ラベル
    lbl_score = tk.Label(frame_prime, text="スコア：0", font=("Arial", 12))
    lbl_score.pack()


    #終了画面
    frame_finish = tk.Frame(frame)
    lbl_finish = tk.Label(frame_finish, text="", font=("Arial", 16))
    lbl_finish.pack(pady=40)
    tk.Button(frame_finish, text= "もう一度遊ぶ", font=("Arial", 12), command= replay).pack(pady=10)
    tk.Button(frame_finish, text= "素数判定ゲームスタート画面に戻る", font=("Arial", 12),command= back_to_start).pack(pady=10)
    if back_to_top:
        tk.Button(frame_finish, text="トップに戻る", font=("Arial", 12), command= back_to_top).pack(pady=10)

#UI
if __name__ == "__main__":
    root = tk.Tk()
    root.title("素数判定ゲーム")
    root.geometry("600x600")
    frame = tk.Frame(root)
    frame.pack()
    build(root,frame)
    root.mainloop()