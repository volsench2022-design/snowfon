import tkinter as tk
import random

class Snowfall:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Снігопад")
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.attributes('-transparentcolor', 'black')
        self.root.overrideredirect(True)  # Прибираємо рамку вікна
        self.canvas = tk.Canvas(self.root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.snowflakes = []
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        for _ in range(150):  # Кількість сніжинок
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            speed_y = random.uniform(1, 4)
            speed_x = random.uniform(-0.5, 0.5)
            size = random.randint(2, 5)
            self.snowflakes.append({'x': x, 'y': y, 'speed_y': speed_y, 'speed_x': speed_x, 'size': size})
        self.animate()
        self.root.mainloop()

    def animate(self):
        self.canvas.delete('all')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        for flake in self.snowflakes:
            flake['x'] += flake['speed_x']
            flake['y'] += flake['speed_y']
            if flake['y'] > screen_height:
                flake['y'] = 0
                flake['x'] = random.randint(0, screen_width)
            if flake['x'] < 0:
                flake['x'] = screen_width
            elif flake['x'] > screen_width:
                flake['x'] = 0
            size = flake['size']
            self.canvas.create_oval(flake['x']-size, flake['y']-size, flake['x']+size, flake['y']+size, fill='white', outline='white')
        self.root.after(30, self.animate)

if __name__ == '__main__':
    Snowfall()