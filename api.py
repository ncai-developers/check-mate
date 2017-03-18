import urllib.request
import urllib.parse
import urllib.error
import ast
import requests

# Important Note:
# the functions here serve to use different APIs
# to change which function is used, navigate to main.py and change the function there
# I (Lacayo) will be using login instead of mock for my GUI until mock is up and running

api_url = "http://localhost:3000/api/"

def get_credit_with_login(username, password):
    # function using NCAI login to get credit_student and credit_family

    api = 'http://db.nca.edu.ni/api/api_ewapp.php?'
    data = {
        'mode': 'student',
        'query': 'login',
        'username': username,
        'password': password,
    }
    url = api + urllib.parse.urlencode(data)
    # data must be encoded for url to function properly

    try:
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

    except urllib.error.URLError:
        return 'No internet connection.'

# gets an id as param
# returns a dictionary with name, balance, id, and picture in base64
def get_data(id):
    try:
        response = requests.get(api_url + id).json()
        return response
    except requests.exceptions.RequestException as e:
        print(e)
        return e
