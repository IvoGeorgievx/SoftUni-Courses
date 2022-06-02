import re


def password_validation(password):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    counter = 0

    if len(password) < 6 or len(password) > 10:
        print('Password must be between 6 and 10 characters')
    else:
        counter += 1

    if (regex.search(password) == None):
        counter += 1
    else:
        print("Password must consist only of letters and digits")

    if re.search('[0-9]', password) is None:
        print('Password must have at least 2 digits')
    else:
        counter += 1

    if counter == 3:
        print('Password is valid')


password = input()
password_validation(password)
