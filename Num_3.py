# https://www.codewars.com//kata/57a1fd2ce298a731b20006a4

def is_palindrome(s):
    flag = False
    if s.lower() == s.lower()[::-1]:
        flag = True
    return flag