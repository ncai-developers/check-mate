import tkinter as tk
import api


class Application(tk.Frame):  # for there's only one frame, so this will be the main one
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_window()  # after initial setup; we now setup the window and its parts

    def init_window(self):
        def display_credit():  # use our get_student_credit function and output it to the balance Tk variable
            try:
                output = api.get_credit_with_login(entry_username.get(), entry_password.get())
            except SyntaxError:
                # This happens when the entries are empty
                output = 'Please enter username and password.'
            balance.config(text=output)

        def display_data():
            json = api.get_data( entry_id.get() )
            try:
                text = json["name"] + ": " + str(json["balance"])
            except KeyError as e:
                print(e, "key not found in response")
                text = "Wrong ID. Try again"
            balance.config(text=text)

        # creating the Tk widgets
        entry_id = tk.Entry(self)
        balance = tk.Message(self, width='200')
        button_get_credit = tk.Button(self, text="Fetch Credit", command=display_data)

        self.master.title("Student Credit")
        # displaying the Tk widgets with pack()
        self.pack(fill='both', expand=1)
        entry_id.pack()
        button_get_credit.pack()
        balance.pack()

root = tk.Tk()
root.geometry("350x200")  # sets window size
app = Application(root)
root.mainloop()  # this kicks off tkinter window
