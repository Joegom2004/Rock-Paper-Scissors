import tkinter as tk
from tkinter import messagebox
import random

RPS = ['rock', 'paper', 'scissors']

class RPSGame:
    def __init__(self, master):
        """Initialize the Rock Paper Scissors game GUI."""
        self.master = master
        master.title("Rock Paper Scissors")
        master.configure(bg="#23272F")  # More modern dark background

        self.player_score = 0
        self.cpu_score = 0
        self.round_num = 1

        # Welcome label
        self.label = tk.Label(
            master, text="🪨📄✂️ Rock, Paper, Scissors!",
            font=("Segoe UI", 22, "bold"), fg="#FFB86C", bg="#23272F"
        )
        self.label.pack(pady=(25, 12))

        # Score "card"
        self.score_frame = tk.Frame(master, bg="#282C34", bd=2, relief=tk.RIDGE)
        self.score_frame.pack(pady=8)
        self.score_label = tk.Label(
            self.score_frame, text=self.get_score_text(),
            font=("Segoe UI", 14, "bold"), fg="#8BE9FD", bg="#282C34", padx=20, pady=8
        )
        self.score_label.pack()

        # Result "card"
        self.result_frame = tk.Frame(master, bg="#282C34", bd=2, relief=tk.RIDGE)
        self.result_frame.pack(pady=8)
        self.result_label = tk.Label(
            self.result_frame, text="", font=("Segoe UI", 14, "italic"),
            fg="#50FA7B", bg="#282C34", padx=20, pady=8
        )
        self.result_label.pack()

        # CPU choice label
        self.cpu_choice_label = tk.Label(
            master, text="", font=("Segoe UI", 13, "bold"),
            fg="#FF79C6", bg="#23272F"
        )
        self.cpu_choice_label.pack(pady=5)

        # Frame for choice buttons
        self.button_frame = tk.Frame(master, bg="#23272F")
        self.button_frame.pack(pady=18)

        # Choice buttons with icons/emojis
        icons = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
        self.choice_buttons = []
        for choice in RPS:
            btn = tk.Button(
                self.button_frame,
                text=f"{icons[choice]} {choice.capitalize()}",
                width=14, height=2,
                font=("Segoe UI", 13, "bold"),
                bg="#44475A", fg="#F8F8F2", activebackground="#6272A4",
                activeforeground="#FFB86C",
                command=lambda c=choice: self.play_round(c),
                relief=tk.FLAT, bd=0, cursor="hand2", highlightthickness=2, highlightbackground="#FFB86C"
            )
            btn.pack(side=tk.LEFT, padx=14)
            self.choice_buttons.append(btn)

        # Play Again button (disabled until a round is played)
        self.play_again_btn = tk.Button(
            master, text="🔄 Play Again", command=self.reset, state=tk.DISABLED,
            font=("Segoe UI", 12, "bold"), bg="#50FA7B", fg="#23272F",
            activebackground="#8BE9FD", activeforeground="#23272F",
            width=15, height=1, bd=0, cursor="hand2", relief=tk.FLAT
        )
        self.play_again_btn.pack(pady=(18, 7))

        # Reset Scores button
        self.reset_score_btn = tk.Button(
            master, text="🔁 Reset Scores", command=self.reset_scores,
            font=("Segoe UI", 12, "bold"), bg="#FFB86C", fg="#23272F",
            activebackground="#FF79C6", activeforeground="#23272F",
            width=15, height=1, bd=0, cursor="hand2", relief=tk.FLAT
        )
        self.reset_score_btn.pack(pady=5)

        # Quit button
        self.quit_btn = tk.Button(
            master, text="❌ Quit", command=self.quit_game,
            font=("Segoe UI", 12, "bold"), bg="#44475A", fg="#FF5555",
            activebackground="#282C34", activeforeground="#FF5555",
            width=15, height=1, bd=0, cursor="hand2", relief=tk.FLAT
        )
        self.quit_btn.pack(pady=(5, 20))

    def get_score_text(self):
        """Return the formatted score text."""
        return f"Score ➡️  Player: {self.player_score}   |   CPU: {self.cpu_score}   |   Round: {self.round_num}"

    def play_round(self, player_choice):
        """Handle a round of play."""
        cpu_choice = random.choice(RPS)
        self.cpu_choice_label.config(text=f"🤖 CPU chose: {cpu_choice.capitalize()}")
        result = self.determine_winner(player_choice, cpu_choice)
        if result == 'tie':
            self.result_label.config(
                text=f"Both chose {player_choice}. It's a tie! Try again.",
                fg="#FFB86C"
            )
            return
        elif result == 'player':
            self.player_score += 1
            self.result_label.config(
                text=f"🎉 Player wins! {player_choice.capitalize()} beats {cpu_choice}!",
                fg="#50FA7B"
            )
        else:
            self.cpu_score += 1
            self.result_label.config(
                text=f"💻 CPU wins! {cpu_choice.capitalize()} beats {player_choice}!",
                fg="#FF5555"
            )

        self.score_label.config(text=self.get_score_text())
        self.round_num += 1
        self.disable_buttons()
        self.play_again_btn.config(state=tk.NORMAL)

    def determine_winner(self, player, cpu):
        """Determine the winner of a round."""
        if player == cpu:
            return 'tie'
        wins = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }
        return 'player' if wins[player] == cpu else 'cpu'

    def disable_buttons(self):
        """Disable choice buttons."""
        for btn in self.choice_buttons:
            btn.config(state=tk.DISABLED)

    def enable_buttons(self):
        """Enable choice buttons."""
        for btn in self.choice_buttons:
            btn.config(state=tk.NORMAL)

    def reset(self):
        """Reset the round (not scores)."""
        self.result_label.config(text="", fg="#50FA7B")
        self.cpu_choice_label.config(text="")
        self.enable_buttons()
        self.play_again_btn.config(state=tk.DISABLED)

    def reset_scores(self):
        """Reset scores and round number, and notify the user."""
        self.player_score = 0
        self.cpu_score = 0
        self.round_num = 1
        self.score_label.config(text=self.get_score_text())
        self.reset()
        messagebox.showinfo("Scores Reset", "Scores and round number have been reset!")

    def quit_game(self):
        """Show final score and quit the game."""
        messagebox.showinfo(
            "Final Score",
            f"Thanks for playing!\n\nFinal Score:\nPlayer: {self.player_score}\nCPU: {self.cpu_score}\nRounds played: {self.round_num - 1}"
        )
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()


