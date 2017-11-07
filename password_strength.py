import sys
import re
from string import punctuation


def get_password_blacklist():
    with open('pass.txt', 'r') as file:
        black_list = file.read().split()
        return black_list


def get_password_strength(password):
    rating = 0
    if re.search(r'\d', password):
        rating += 2
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        rating += 2
    if re.search(r'[{}]'.format(punctuation), password):
        rating += 4
    password_blacklist = get_password_blacklist()
    if password_blacklist.count(password) > 0:
        rating = 1
    else:
        rating += 2
    return rating


if __name__ == '__main__':
    password = sys.argv[1]
    print(get_password_strength(password))
