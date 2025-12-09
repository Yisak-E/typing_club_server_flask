import math
import tkinter as tk

from server.view.TypingPage import TypingPage


class Animation(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # start size
        self.start_radius = 80  # Reduced start radius
        self.target_radius = 120  # Reduced target radius
        self.duration = 2000
        self.steps = 60
        self.step_time = self.duration // self.steps
        self.d_radius = (self.target_radius - self.start_radius) / self.steps



        # Create larger canvas to accommodate all circles
        self.canvas = tk.Canvas(self, bg="darkgray", width=800, height=450, highlightthickness=0)
        self.canvas.pack(pady=10)  # Reduced padding

        # Center the circle in the canvas with proper margins
        self.center_x = 400
        self.center_y = 225  # Centered in 450px height canvas

        self.circle = self.canvas.create_oval(
            self.center_x - self.start_radius,
            self.center_y - self.start_radius,
            self.center_x + self.start_radius,
            self.center_y + self.start_radius,
            fill="black",
            outline="white",
            width=2,
            tags="main_circle"
        )

        self.text_id = self.canvas.create_text(
            self.center_x, self.center_y,
            text="News Hub",
            font=("Arial", 14, "bold"),
            fill="white"
        )

        self.canvas.tag_bind("main_circle", "<Button-1>", self.on_main_circle_click)

        self.animate_step(0)

    def on_main_circle_click(self, event):
        item = self.canvas.find_closest(event.x, event.y)[0]
        tags = self.canvas.gettags(item)

        if "main_circle" in tags:
            page_2 = TypingPage(self)







    def animate_step(self, step):
        if step <= self.steps:
            current_radius = self.start_radius + (self.d_radius * step)

            self.canvas.coords(self.circle,
                               self.center_x - current_radius,
                               self.center_y - current_radius,
                               self.center_x + current_radius,
                               self.center_y + current_radius)

            font_size = max(14, int(14 * (current_radius / self.start_radius)))
            self.canvas.itemconfig(self.text_id, font=("Arial", font_size, "bold"))

            self.canvas.after(self.step_time, lambda: self.animate_step(step + 1))
        else:
            self.add_news_content()

    def add_news_content(self):
        news_items = [
            "Tech",
            "Sports",
            "Weather",
            "Business",
            "Politics",
            "Health"
        ]

        # Calculate safe radius to prevent cutting
        satellite_radius = 35  # Smaller satellite circles
        margin = 20  # Margin from canvas edges

        # Maximum possible radius without cutting
        max_safe_radius = min(
            self.center_x - satellite_radius - margin,  # Horizontal limit
            self.center_y - satellite_radius - margin  # Vertical limit
        )

        radius = min(self.target_radius + 80, max_safe_radius)

        for i, item in enumerate(news_items):
            angle = 2 * math.pi * i / len(news_items)
            x = self.center_x + radius * math.cos(angle)
            y = self.center_y + radius * math.sin(angle)

            # Create news category circles
            news_circle = self.canvas.create_oval(
                x - satellite_radius,
                y - satellite_radius,
                x + satellite_radius,
                y + satellite_radius,
                fill="black",
                outline="white",
                width=2
            )

            self.canvas.create_text(
                x, y,
                text=item,
                font=("Arial", 8, "bold"),
                fill="white"
            )

