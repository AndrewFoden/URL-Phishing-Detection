import tkinter as tk

class UserInterface:

    def __init__(self):
        self.LoadWindow()

    def LoadWindow(self):
        root = tk.Tk()
        root.title("URL Phishing Detector")
        root.geometry("700x500")
        root.mainloop()


main = UserInterface()