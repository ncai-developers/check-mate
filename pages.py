import tkinter as tk


class Welcome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="This is the Welcome Page")
        button1 = tk.Button(self, text="Go to PageBalance",
                            command=lambda: controller.show_frame('Balance'))
        label1.pack()
        button1.pack()


class Balance(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="This is the Balance Page")
        button1 = tk.Button(self, text="Go to PageProduct",
                            command=lambda: controller.show_frame('Product'))
        label1.pack()
        button1.pack()


class Product(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="This is the Product Page")
        button1 = tk.Button(self, text="Go to PageThankYou",
                            command=lambda: controller.show_frame('ThankYou'))
        label1.pack()
        button1.pack()


class ThankYou(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="This is the Thank You Page")
        button1 = tk.Button(self, text="Return to Welcome Page",
                            command=lambda: controller.show_frame('Welcome'))
        label1.pack()
        button1.pack()