import urllib.request
import urllib.parse
import urllib.error
import ast
import tkinter as tk


def get_student_credit(username, password):
    # function that takes the NCA username and password, and returns the balance

    api = 'http://db.nca.edu.ni/api/api_ewapp.php?'
    data = {
        'mode': 'student',
        'query': 'login',
        'username': username,
        'password': password,
    }
    url = api + urllib.parse.urlencode(data)
    # data must be encoded for url to function properly

    with urllib.request.urlopen(url) as response:
        page_raw = response.read()      # get page source; but it's encoded
        page_str = page_raw.decode()    # decode the source; now a string

        if 'null' in page_str:
            return "Error with login, please try again."
            # when there's a login error, nulls will be present
            # we can check a login error by checking for nulls
        else:
            page_dict = ast.literal_eval(page_str)  # evaluate the page str; now it's a python dictionary
            credit_student = page_dict['credit_student']  # get value of key 'credit_student'
            credit_family = page_dict['credit_family'] # get value of key 'credit_family'
            return "Student Credit: ${} \nFamily Credit:   ${}".format(credit_student, credit_family)


class Application(tk.Frame):  # for there's only one frame, so this will be the main one
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_window()  # after initial setup; we now setup the window and its parts

    def init_window(self):
        def display_credit():  # use our get_student_credit function and output it to the text1 Tk variable
            try:
                output = get_student_credit(entry_username.get(), entry_password.get())
            except SyntaxError:  # If the entries are empty and you use get(), returns SyntaxError
                output = 'Please enter username and password.'
            except urllib.error.URLError:
                output = 'No internet connection.'

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
