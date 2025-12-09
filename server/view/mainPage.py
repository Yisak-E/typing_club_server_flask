import tkinter as tk
from landingPage import Animation
from TypingPage import TypingPage

class MainPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("News Hub")
        self.geometry("800x500")
        self.configure(bg="lightgray")
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.main_page = Animation(self.container)
        self.typing_page = TypingPage(self.container)

        self.show_main_page()


    def get_root(self):
        return self


    def show_main_page(self):
        self.typing_page.pack_forget()
        self.main_page.pack(fill="both", expand=True)


    def show_typing_page(self):
        self.main_page.pack_forget()
        self.typing_page.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = MainPage()
    animation = Animation(root)
    root.mainloop()