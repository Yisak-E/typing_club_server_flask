import tkinter as tk
class TypingPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.home_page = self.master.master



        frame = tk.Frame(self, bg="white")
        top_frame = tk.Frame(frame, bg="black")
        top_frame.grid(row=0, column=0)
        bottom_frame = tk.Frame(frame, bg="black")
        bottom_frame.grid(row=1, column=0)
        bottom_frame.grid_rowconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(0, weight=1)




