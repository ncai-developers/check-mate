
import requests


def get_credit_with_mock(user_id):
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

def get_credit_in_cords_with_mock(user_id):
    try:
        api = "http://localhost:3000/api/"
        response = requests.get(api + user_id).json()
        return "Balance: C$ {}\nFamily balance: C${}".format(response['credit_student']*29.5, response['credit_family']*29.5)
    except requests.exceptions.ConnectionError:
        return "Connection unable to be established. Is the server online?"
    except KeyError:
        return "Invalid id. Please try again."
    except TypeError:
        return "Please enter an id"
    except KeyboardInterrupt:
        return "Goodbye"
