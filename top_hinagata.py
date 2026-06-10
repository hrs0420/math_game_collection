import tkinter as tk
import random
import prime_factorization
import prime_number

def go_menu():
    frame_prime_factors.pack_forget()
    frame_prime_quiz.pack_forget()
    frame_menu.pack()

def go_prime_factors():
    frame_menu.pack_forget()
    frame_prime_factors.pack()

def go_prime_quiz():
    frame_menu.pack_forget()
    frame_prime_quiz.pack()


root = tk.Tk()
root.title("数学ゲームコレクション")
root.geometry("600x600")

#メニュー画面
frame_menu = tk.Frame(root)
frame_menu.pack()
frame_prime_factors = tk.Frame(root)
frame_prime_quiz = tk.Frame(root)

prime_factorization.build(root, frame_prime_factors, back_to_top= go_menu)
prime_number.build(root, frame_prime_quiz, back_to_top= go_menu)

tk.Label(frame_menu, text= "数学ゲームコレクション", font=("Arial", 20)).pack(pady=30)
tk.Button(frame_menu, text = "素因数分解ゲーム", font= ("Arial", 14),command= go_prime_factors).pack(pady=10)
tk.Button(frame_menu, text= "素数判定クイズ", font= ("Arial", 14),command= go_prime_quiz).pack(pady=10)

root.mainloop()