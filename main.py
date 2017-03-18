import tkinter as tk
import api


class Application(tk.Frame):  # for there's only one frame, so this will be the main one
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_window()  # after initial setup; we now setup the window and its parts

    def init_window(self):
        def display_credit():  # use our get_student_credit function and output it to the text1 Tk variable
            try:
                output = api.get_credit_with_login(entry_username.get(), entry_password.get())
            except SyntaxError:
                # This happens when the entries are empty
                output = 'Please enter username and password.'
            text1.config(text=output)

        entry_username = tk.Entry(self)  # creating the Tk widgets
        entry_password = tk.Entry(self, show='*')
        text1 = tk.Message(self, width='200')
        button_get_credit = tk.Button(self, text="Fetch Credit", command=display_credit)

        self.master.title("Student Credit")
        self.pack(fill='both', expand=1)  # displaying the Tk widgets with pack()
        entry_username.pack()
        entry_password.pack()
        button_get_credit.pack()
        text1.pack()

root = tk.Tk()
root.geometry("250x100")  # sets window size
app = Application(root)
root.mainloop()  # this kicks off tkinter window
