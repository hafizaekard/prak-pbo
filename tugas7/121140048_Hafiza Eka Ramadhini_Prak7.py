import tkinter as tk
import random

class Game:
    def __init__(self, master):
        self.master = master
        master.title("Tebak Angka")

        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Tebak angka antara 1 dan 100")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Tebak", command=self.check_guess)
        self.button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.reset_button = tk.Button(master, text="Ulangi", command=self.reset_game)
        self.reset_button.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.attempts += 1

        if guess < self.target_number:
            self.result_label.config(text="Angka terlalu kecil")
        elif guess > self.target_number:
            self.result_label.config(text="Angka terlalu besar")
        else:
            self.result_label.config(text="Tebakan benar! Angka yang dicari adalah " + str(self.target_number))

        self.entry.delete(0, tk.END)

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")


root = tk.Tk()
game = Game(root)
root.mainloop()
