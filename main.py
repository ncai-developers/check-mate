import urllib.request
import urllib.parse
import ast

def get_student_credit(username, password):
    api = 'http://db.nca.edu.ni/api/api_ewapp.php?'
    data = {
        'mode': 'student',
        'query': 'login',
        'username': username,
        'password': password,
        }
    url = api + urllib.parse.urlencode(data)
    # creates the url with the 
    
    with urllib.request.urlopen(url) as response:
        page_raw = response.read()
        page_str = page_raw.decode()
        page_dict = ast.literal_eval(page_str)
        credit_student_amount = page_dict['credit_student']
        
        if page_dict['login'] == 0:
            print("Error with login, please try again.")
        elif page_dict['login'] == 1:
            print(credit_student_amount)

get_student_credit(input("Username: "), input("Password: "))
# main function that takes the NCA username and password everyone has
