import tkinter as tk
from tkinter import colorchooser


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Простой Paint на Python")

        # Настройка холста
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.color = "black"  # Начальный цвет
        self.last_x, self.last_y = None, None

        # Кнопка выбора цвета
        self.color_button = tk.Button(self.root, text="Выбрать цвет", command=self.choose_color)
        self.color_button.pack()

        # Очистить кнопку
        self.clear_button = tk.Button(self.root, text="Очистить", command=self.clear_canvas)
        self.clear_button.pack()

        # Подключаем события для рисования
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def choose_color(self):
        # Открываем диалог для выбора цвета
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def paint(self, event):
        # Рисование на холсте
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, width=5, fill=self.color,
                                    capstyle=tk.ROUND, smooth=True)
        self.last_x = event.x
        self.last_y = event.y

    def reset(self, event):
        # Сбрасываем последние координаты
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        # Очищаем холст
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
