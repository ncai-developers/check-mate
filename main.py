import tkinter as tk
import api
import pages


class Application(tk.Tk):  # for there's only one frame, so this will be the main one

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # self.overrideredirect(1)  # removes title bar
        # self.geometry("{}x{}".format(tk.Tk.winfo_screenwidth(self), tk.Tk.winfo_screenheight(self)))
        self.state('zoomed')  # full-screen without removing title bar

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.load_frames((pages.Welcome, pages.Balance, pages.Product, pages.ThankYou))

        self.show_frame("Welcome")

    def load_frames(self, frames):
        """
        This fills self.frames by cycling through all of the pages created in pages.py
        __name__: instance
        display each frame using grid()
        """
        for F in frames:
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        """
        Order matters; each frame is shown, but only one can be displayed.
        To move a frame to the top of the order (thus display it), call
        this function to load the page using it's name, e.g. "Welcome"
        """
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == '__main__':
    app = Application()
    app.mainloop()
