import tkinter as tk

class UserInterface:

    def __init__(self):
        self.LoadWindow()

    def LoadWindow(self):
        root = tk.Tk()
        root.title("URL Phishing Detector")
        root.geometry("700x500")
        root.configure(bg="lightgrey")



        title = tk.Label(root, text="URL Phishing Detector", font=("Arial",30))
        title.place(x=150,y=40)

        box = tk.Frame(root, bd=3, relief="solid", bg="darkgrey")
        box.place(x=100, y=170, width=500, height=300)

        label = tk.Label(root, text="Input a URL:", font=("Arial",20))
        label.place(x=140,y=230)

        self.entry_box = tk.Entry(root, width=40)
        self.entry_box.place(x=310,y=250)

        entry_button = tk.Button(root, text="Enter", font=("Arial", 14), command=self.getInput())
        entry_button.place(x=300,y=320)


        root.mainloop()

    def getInput(self):
        input = self.entry_box.get()
        print(input)


main = UserInterface()