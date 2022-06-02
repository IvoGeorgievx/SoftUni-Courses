def is_palindrome(num):
    for i in num:
        if i == i[::-1]:
            print('True')
        else:
            print('False')


the_num = input().split(", ")
is_palindrome(the_num)
