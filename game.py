import tkinter as tk
import random

def roll_dice():
    result = random.randint(1, 6)
    result_label.config(text=f"Wynik: {result}")


root = tk.Tk()
root.title("Rzut kostką")
root.geometry("200x150")


result_label = tk.Label(root, text="Kliknij, aby rzucić kostką", font=("Arial", 12))
result_label.pack(pady=20)


roll_button = tk.Button(root, text="Rzuć kostką", command=roll_dice)
roll_button.pack()


root.mainloop()
