import tkinter as tk

class UserInterface:

    def __init__(self):
        self.LoadWindow()

    def LoadWindow(self):
        root = tk.Tk()
        root.title("URL Phishing Detector")
        root.geometry("700x500")
        root.configure(bg="lightblue")

        label = tk.Label(root, text="Enter a URL:", font=("Arial",20))
        label.pack(pady=230)

        entry_box = tk.Entry(root, width=40)
        entry_box.place(x=250,y=300)

        root.mainloop()


main = UserInterface()