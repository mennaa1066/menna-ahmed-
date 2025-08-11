import random
import tkinter as tk
from tkinter import messagebox

WORD_LEN = 5
MAX_ATTEMPTS = 6

def load_words(filepath):
    with open(filepath, "r") as f:
        return [w.strip().lower() for w in f if len(w.strip()) == WORD_LEN]

class WordleGUI:
    def __init__(self, master, secret, valid_words):
        self.master = master
        self.secret = secret
        self.words = valid_words
        self.attempt = 0

        master.title("Wordle")
        self.create_grid()
        self.create_entry()

    def create_grid(self):
        self.grid_labels = []
        frame = tk.Frame(self.master)
        frame.pack(pady=10)
        for _ in range(MAX_ATTEMPTS):
            row = []
            for _ in range(WORD_LEN):
                lbl = tk.Label(frame, text="", width=4, height=2, font=("Arial", 18), relief="solid", bd=1)
                lbl.pack(side=tk.LEFT, padx=2, pady=2)
                row.append(lbl)
            self.grid_labels.append(row)

    def create_entry(self):
        self.info_label = tk.Label(self.master, text="Enter your guess")
        self.info_label.pack()
        self.entry = tk.Entry(self.master, width=8, font=("Arial", 16))
        self.entry.pack()
        self.entry.bind("<Return>", self.submit_guess)

    def submit_guess(self, event=None):
        guess = self.entry.get().lower()
        if len(guess) != WORD_LEN:
            self.info_label.config(text="Word must be 5 letters", fg="red")
            return
        if guess not in self.words:
            self.info_label.config(text="Not in dictionary", fg="red")
            return

        # Update grid colors
        for i, ch in enumerate(guess):
            lbl = self.grid_labels[self.attempt][i]
            lbl.config(text=ch.upper())
            if ch == self.secret[i]:
                color = "#6aaa64"  # green
            elif ch in self.secret:
                color = "#c9b458"  # yellow
            else:
                color = "#787c7e"  # gray
            lbl.config(bg=color, fg="white")

        self.attempt += 1
        self.entry.delete(0, tk.END)

        if guess == self.secret:
            self.win_game()
        elif self.attempt >= MAX_ATTEMPTS:
            self.lose_game()
        else:
            self.info_label.config(text=f"Attempt {self.attempt+1}/{MAX_ATTEMPTS}", fg="black")

    def win_game(self):
        messagebox.showinfo("Wordle", f"You guessed it! The word was {self.secret.upper()}")
        self.entry.config(state=tk.DISABLED)

    def lose_game(self):
        messagebox.showinfo("Wordle", f"Out of tries! The word was {self.secret.upper()}")
        self.entry.config(state=tk.DISABLED)

if __name__ == "__main__":
    words = load_words("words.txt")
    secret_word = random.choice(words)
    root = tk.Tk()
    app = WordleGUI(root, secret_word, words)
    root.mainloop()
