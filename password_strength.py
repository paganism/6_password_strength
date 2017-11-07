import sys


def get_password_blacklist():
    with open('pass.txt', 'r') as file:
        black_list = file.read().split()
        return black_list


def get_password_strength(password):
    lower_case = 0
    upper_case = 0
    digit_case = 0
    spec_char = 0
    rating = 0
    for letter in password:
        if letter.isupper():
            upper_case += 1
        elif letter.isdigit():
            digit_case += 1
        elif not letter.isalpha() and not letter.isdigit():
            spec_char += 1
        else:
            lower_case += 1
    if upper_case > 0 and lower_case > 0:
        rating += 2
        # print("upper and lower", rating)
    if digit_case > 0:
        rating += 2
        # print("digit", rating)
    if spec_char > 0:
        rating += 4
        # print("spec", rating)
    password_blacklist = get_password_blacklist()
    if password_blacklist.count(password) > 0:
        # print("your password is in blacklist")
        rating = 1
    else:
        rating += 2
    return rating


if __name__ == '__main__':
    password = sys.argv[1]
    print(get_password_strength(password))
