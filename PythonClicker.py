import tkinter as tk


class ClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker")
        self.root.geometry("300x200")

        self.score = 0
        self.level = 1
        self.next_level_threshold = 50
        self.click_power = 1

        self.label = tk.Label(root, text="Score: 0", font=("Helvetica", 18))
        self.label.pack(pady=20)

        self.level_label = tk.Label(root, text="Level: 1", font=("Helvetica", 16))
        self.level_label.pack(pady=5)

        self.button = tk.Button(root, text="Click Me", font=("Helvetica", 14), command=self.click)
        self.button.pack(pady=10)

        self.upgrade_button = tk.Button(root, text="improve (+1 to click) - 100 points", command=self.upgrade_click)
        self.upgrade_button.pack(pady=10)


    def click(self):
        self.score += self.click_power
        self.label.config(text=f"Score: {self.score}")

        if self.score >= self.next_level_threshold:
            self.level += 1
            self.next_level_threshold += 50
            self.level_label.config(text=f"Level: {self.level}")


    def upgrade_click(self):
        if self.score >= 100:
            self.score -= 100
            self.click_power += 1
            self.label.config(text=f"Score: {self.score}")
            self.upgrade_button.config(text=f"Improve (+1 to click) - 100 points")




if __name__ == "__main__":
    root = tk.Tk()
    app = ClickerApp(root)
    root.mainloop()


