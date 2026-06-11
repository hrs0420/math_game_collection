import tkinter as tk
import random
import prime_factorization
import prime_number
import make10_puzzle

#メニュー画面に戻る用の関数
def go_menu():
    frame_prime_factors.pack_forget()
    frame_prime_quiz.pack_forget()
    frame_make10_puzzle.pack_forget()
    frame_menu.pack()

#素因数分解ゲーム
def go_prime_factors():
    frame_menu.pack_forget()
    frame_prime_factors.pack()
    prime_factorization.reset()

#素数判定クイズ
def go_prime_quiz():
    frame_menu.pack_forget()
    frame_prime_quiz.pack()
    prime_number.reset()
    
#Make10パズル
def go_make10_puzzle():
    frame_menu.pack_forget()
    frame_make10_puzzle.pack()
    make10_puzzle.reset()

#初期化用の関数
def reset():
    frame_game.pack_forget()
    frame_finish.pack_forget()
    frame_how_to.pack_forget()
    frame_start.pack()


root = tk.Tk()
root.title("数学ゲームコレクション")
root.geometry("600x600")

#メニュー画面
frame_menu = tk.Frame(root)
frame_menu.pack()
frame_prime_factors = tk.Frame(root)
frame_prime_quiz = tk.Frame(root)
frame_make10_puzzle = tk.Frame(root)

prime_factorization.build(root, frame_prime_factors, back_to_top= go_menu)
prime_number.build(root, frame_prime_quiz, back_to_top= go_menu)
make10_puzzle.build(root, frame_make10_puzzle, back_to_top= go_menu)


tk.Label(frame_menu, text= "数学ゲームコレクション", font=("Arial", 20)).pack(pady=30)
tk.Button(frame_menu, text = "素因数分解ゲーム", font= ("Arial", 14),command= go_prime_factors).pack(pady=10)
tk.Button(frame_menu, text= "素数判定クイズ", font= ("Arial", 14),command= go_prime_quiz).pack(pady=10)
tk.Button(frame_menu, text= "Make10パズル", font=("Arial", 14), command= go_make10_puzzle).pack(pady=10)
root.mainloop()