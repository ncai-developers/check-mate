import tkinter as tk

font_types = {
    'title': ('Helvetica', 18, 'bold'),
    'subtitle': ('Helvetica', 12, 'bold'),
    'normal': ('Helvetica', 10),
}


def spawn_image(parent, file):
    """Returns a label with an image inside it
    
    Keyword arguments:
    parent -- the container that is the main frame
    file -- location of image; must be .gif
    """
    photo = tk.PhotoImage(file=file)
    label = tk.Label(parent, image=photo)
    label.image = photo
    return label


class Welcome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(background='red')
        label_text1 = tk.Label(self, text="This is the Welcome Page", font=font_types['title'])
        label_text2 = tk.Label(self, text="We hope you enjoy your stay!", font=font_types['subtitle'])
        label_text3 = tk.Label(self, text="Please scan card", font=font_types['normal'])
        button1 = tk.Button(self, text="Go to PageBalance",
                            command=lambda: self.controller.show_frame('Balance'))

        label_text1.pack()
        label_text2.pack()
        label_text3.pack()
        spawn_image(self, 'images/card_start.gif').pack()
        spawn_image(self, 'images/good_start.gif').pack()
        button1.pack()


class Balance(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="This is the Balance Page")
        button1 = tk.Button(self, text="Go to PageProduct",
                            command=lambda: self.controller.show_frame('Product'))
        label1.pack()
        button1.pack()


class Product(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="This is the Product Page")
        button1 = tk.Button(self, text="Go to PageThankYou",
                            command=lambda: self.controller.show_frame('ThankYou'))
        label1.pack()
        button1.pack()


class ThankYou(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="This is the Thank You Page")
        button1 = tk.Button(self, text="Return to Welcome Page",
                            command=lambda: self.controller.show_frame('Welcome'))
        label1.pack()
        button1.pack()
