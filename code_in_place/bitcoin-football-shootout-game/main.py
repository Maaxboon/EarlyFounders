import tkinter as tk
import random

# Constants
GOAL_REWARD_BTC = 0.001
DIRECTIONS = ['Left', 'Center', 'Right']

class PenaltyShootoutGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Bitcoin Penalty Shootout ⚽ ₿")
        self.root.geometry("500x400")
        self.root.config(bg="green")

        # Game state
        self.score = 0
        self.bitcoin = 0.0
        self.rounds = 0

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Penalty Shootout", font=("Arial", 24, "bold"), bg="green", fg="white")
        self.title_label.pack(pady=10)

        self.info_label = tk.Label(self.root, text="Click a direction to shoot!", font=("Arial", 14), bg="green", fg="white")
        self.info_label.pack(pady=10)

        # Direction buttons
        self.button_frame = tk.Frame(self.root, bg="green")
        self.button_frame.pack()

        for direction in DIRECTIONS:
            btn = tk.Button(
                self.button_frame,
                text=direction,
                font=("Arial", 12, "bold"),
                width=10,
                command=lambda dir=direction: self.shoot(dir)
            )
            btn.pack(side=tk.LEFT, padx=10, pady=10)

        # Result display
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), bg="green", fg="yellow")
        self.result_label.pack(pady=10)

        # Scoreboard
        self.score_label = tk.Label(self.root, text=self.get_score_text(), font=("Arial", 12), bg="green", fg="white")
        self.score_label.pack(pady=10)

    def get_score_text(self):
        return f"Goals Scored: {self.score}  |  BTC Earned: {self.bitcoin:.4f}"

    def shoot(self, player_direction):
        goalie_direction = random.choice(DIRECTIONS)
        self.rounds += 1

        if player_direction == goalie_direction:
            self.result_label.config(text=f"Saved! Goalie went {goalie_direction} 😬")
        else:
            self.result_label.config(text=f"Goal! Goalie went {goalie_direction} 🎯")
            self.score += 1
            self.bitcoin += GOAL_REWARD_BTC

        self.score_label.config(text=self.get_score_text())

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = PenaltyShootoutGame(root)
    root.mainloop()
