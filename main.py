import urllib.request
import urllib.parse
import ast
import getpass
import sys


def get_student_credit(username, password):
    # function that takes the NCA username and password, and outputs the credit student balance
    
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
        page_raw = response.read()
        page_str = page_raw.decode()
        
        if 'null' in page_str:
            print("Error with login, please try again.")
            # python doesn't know what null means, so it cannot be evaluated
            # any typos will create null, thus raising an exception, so we'll
            # end the function in this if statement
        else:
            page_dict = ast.literal_eval(page_str)
            credit_student_balance = page_dict['credit_student']
            print(credit_student_balance)

while True:
    try:
        get_student_credit(input("Username: "), getpass.getpass())
    except KeyboardInterrupt:
        sys.exit(0)
        # Control-C will raise a KeyboardInterrupt exception, our method of quitting
