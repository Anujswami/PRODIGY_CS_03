#Python script to check Password Strength

def length_checker(password):
    if len(password) < 12:
        return "Password is too short, it should be at least 12 characters long."
    return None

def upper_case_checker(password):
    if not any(c.isupper() for c in password):
        return "Password does not have any uppercase letter."
    return None

def alphabet_checker(password):
    if not any(c.isalpha() for c in password):
        return "Password does not have any alphabet."
    return None

def number_checker(password):
    if not any(c.isdigit() for c in password):
        return "Password does not have any number character."
    return None

def special_character_checker(password):
    special_characters = set('[@_!#$%^&/\'"|()~`]')
    if not any(c in special_characters for c in password):
        return "Password does not have any special character."
    return None

def password_checker(password):
    if not password:
        print("The input was empty.")
        return
    
    checks = [
        length_checker,
        upper_case_checker,
        alphabet_checker,
        number_checker,
        special_character_checker
    ]
    
    issues = [check(password) for check in checks]
    issues = [issue for issue in issues if issue is not None]
    
    if issues:
        for issue in issues:
            print(issue)
    else:
        print("Your password is good.")

user_input = input("Enter Your Password: ")
password_checker(user_input)
