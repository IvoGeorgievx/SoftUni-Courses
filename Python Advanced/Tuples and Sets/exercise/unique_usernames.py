usernames = set()

number_of_usernames = int(input())

for _ in range(number_of_usernames):
    current_user = input()
    usernames.add(current_user)

for i in usernames:
    print(i)