import string


def valid_username():
    allowed = string.digits + string.ascii_letters + '-' + '_'
    usernames = input().split(", ")

    for username in usernames:
        flag = 0
        if 3 > len(username) or len(username) > 16:
            flag = 1

        elif len([x for x in username if x in allowed]) != len(username):
            flag = 1

        if flag == 0:
            print(username)


valid_username()
