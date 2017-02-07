import urllib.request
import urllib.parse
import ast

def get_student_credit(username, password):
    url = 'http://db.nca.edu.ni/api/api_ewapp.php?'
    data = {'mode': 'student',
              'query': 'login',
              'username': username,
              'password': password}
    access = url + urllib.parse.urlencode(data)
    
    with urllib.request.urlopen(access) as response:
       student_credit = ast.literal_eval(response.read().decode())['credit_student']
       # the above reads the page, decodes it (byte to str), evals it as a dictionary, then 
       # gets the value of 'credit_student' and stores it into the variable student_credit
       print(student_credit)

get_student_credit(input(), input())
