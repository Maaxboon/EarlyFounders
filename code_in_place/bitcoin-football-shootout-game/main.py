import tkinter as tk
import random

# Constants
GOAL_REWARD_BTC = 0.001
DIRECTIONS = ['Left', 'Center', 'Right']

# Leaderboard for current session
leaderboard = {}

class PenaltyShootoutGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Bitcoin Penalty Shootout ⚽ ₿")
        self.root.geometry("600x500")
        self.root.config(bg="green")

        # Initial game state
        self.username = ""
        self.score = 0
        self.bitcoin = 0.0
        self.rounds = 0

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()

        self.name_label = tk.Label(self.root, text="Enter your name:", font=("Arial", 16), bg="green", fg="white")
        self.name_label.pack(pady=20)

        self.name_entry = tk.Entry(self.root, font=("Arial", 14))
        self.name_entry.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Game", font=("Arial", 14, "bold"), command=self.start_game)
        self.start_button.pack(pady=10)

    def start_game(self):
        self.username = self.name_entry.get().strip()
        if not self.username:
            self.name_label.config(text="Please enter a name!", fg="red")
            return
        self.create_game_screen()

    def create_game_screen(self):
        self.clear_screen()

        self.title_label = tk.Label(self.root, text=f"{self.username}'s Shootout", font=("Arial", 20, "bold"), bg="green", fg="white")
        self.title_label.pack(pady=10)

        self.info_label = tk.Label(self.root, text="Choose where to shoot!", font=("Arial", 14), bg="green", fg="white")
        self.info_label.pack(pady=5)

        self.button_frame = tk.Frame(self.root, bg="green")
        self.button_frame.pack(pady=10)

        for direction in DIRECTIONS:
            btn = tk.Button(
                self.button_frame,
                text=direction,
                font=("Arial", 12, "bold"),
                width=10,
                command=lambda dir=direction: self.shoot(dir)
            )
            btn.pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), bg="green", fg="yellow")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text=self.get_score_text(), font=("Arial", 12), bg="green", fg="white")
        self.score_label.pack(pady=10)

        self.leaderboard_title = tk.Label(self.root, text="Leaderboard", font=("Arial", 14, "bold"), bg="green", fg="orange")
        self.leaderboard_title.pack(pady=5)

        self.leaderboard_text = tk.Label(self.root, text="", font=("Arial", 12), bg="green", fg="white")
        self.leaderboard_text.pack()

        self.update_leaderboard()

    def get_score_text(self):
        return f"Goals: {self.score} | BTC: {self.bitcoin:.4f}"

    def shoot(self, player_direction):
        goalie_direction = random.choice(DIRECTIONS)

        if player_direction == goalie_direction:
            result = "Saved by the Goalie! 😬"
        else:
            chance = random.random()
            if chance <= 0.7:
                result = "GOAL! 🎯"
                self.score += 1
                self.bitcoin += GOAL_REWARD_BTC
            else:
                result = "You Missed the Goal! 😢"

        self.rounds += 1
        self.result_label.config(text=f"{result} (Goalie went {goalie_direction})")
        self.score_label.config(text=self.get_score_text())

        # Update leaderboard
        leaderboard[self.username] = round(self.bitcoin, 4)
        self.update_leaderboard()

    def update_leaderboard(self):
        sorted_board = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        text = "\n".join([f"{name}: {btc:.4f} BTC" for name, btc in sorted_board])
        self.leaderboard_text.config(text=text)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = PenaltyShootoutGame(root)
    root.mainloop()
