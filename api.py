
import requests

# Important Note:
# the functions here serve to use different APIs
# to change which function is used, navigate to main.py and change the function there
# I (Lacayo) will be using login instead of mock for my GUI until mock is up and running

api = "http://localhost:3000/api/"

def get_credit_with_mock(user_id):
    # function using NCAI login to get credit_student and credit_family
    try:
        api = "http://localhost:3000/api/"
        response = requests.get(api + user_id).json()
        return "Balance: ${}\nFamily balance: ${}".format(response['credit_student'], response['credit_family'])
    except requests.exceptions.ConnectionError:
        return "Connection unable to be established. Is the server online?"
    except KeyError:
        return "Invalid id. Please try again."
    except TypeError:
        return "Please enter an id"
    except KeyboardInterrupt:
        return "Goodbye"
  
        
