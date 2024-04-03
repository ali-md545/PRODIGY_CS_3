#Task 3- Password Complexity Checker by Muhammad Ali Raja

import re

def check_length(password):
    if len(password) >= 8:
        return True
    else:
        return False

def check_uppercase(password):
    if re.search(r'[A-Z]', password):
        return True
    else:
        return False

def check_lowercase(password):
    if re.search(r'[a-z]', password):
        return True
    else:
        return False

def check_digit(password):
    if re.search(r'\d', password):
        return True
    else:
        return False

def check_special_char(password):
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return True
    else:
        return False

def check_common_password(password):
    common_passwords = ['password', '123456', 'qwerty', 'abc123', 'Password123', 'Password123!', 'asdf123'] # Add more common passwords if needed, or read a wordlist containing common passwords
    if password.lower() in common_passwords:
        return False
    else:
        return True


def assess_password_strength(password):
    checks = [check_length, check_uppercase, check_lowercase, check_digit, check_special_char, check_common_password]
    strength = 0
    feedback = []

    for check in checks:
        if check(password):
            strength += 1
        else:
            feedback.append(check.__name__.replace('check_', '').replace('_', ' '))

    if strength < 5:
        feedback.append('Your password is weak. Please strengthen it by following the recommendations above.')
    elif strength < 7:
        feedback.append('Your password is moderate.')
    else:
        feedback.append('Your password is strong.')

    return feedback

if __name__ == "__main__":
    password = input("Enter your password: ")
    feedback = assess_password_strength(password)
    print('\n'.join(feedback))


