import tkinter as tk

class UserInterface:

    def __init__(self, input_callback):
        self.url_input_callback = input_callback
        print("UI INIT")
        self.LoadWindow()
        print("return")



    def LoadWindow(self):
        print("LoadWindow")
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

        entry_button = tk.Button(root, text="Enter", font=("Arial", 14), command=self.getInput)
        entry_button.place(x=300,y=320)

        self.result = tk.Label(root, text="", font=("Arial", 14), fg="blue", bg="lightgrey")
        self.result.place(x=260, y=380)

        root.mainloop()

    def getInput(self):
        print("getInput")
        url = self.entry_box.get()
        if url:
            decision = self.url_input_callback(url)
            self.result.config(text="Predicted: " + decision)
        #print("button")
        #print(input)



    def phishingURL(self):
        pass

    def beningURL(self):
        pass


#ui = UserInterface()