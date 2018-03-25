import sys
import re
from string import punctuation
import getpass


def get_password_blacklist():
    with open('pass.txt', 'r') as file:
        black_list = file.read().split('\n')
        return black_list


def get_password_strength(password):
    length_criteria = 6
    rating = 0
    password_blacklist = get_password_blacklist()
    if password in password_blacklist:
        rating = 1
        sys.exit('Password in black list. Exit...')
    if re.search(r'\d', password):
        rating += 2
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        rating += 2
    if re.search(r'[{}]'.format(punctuation), password):
        rating += 3
    if len(password) > length_criteria:
        rating +=1
    else:
        rating += 2
    return rating


if __name__ == '__main__':
    password = getpass.getpass()
    print(get_password_strength(password))
