def password_check():
    password = input("Введите пороль: от 10 символов ")
    check_len = False
    check_lower = False
    check_digit = False
    check_upper = False


    if len(password) >= 10:
        check_len = True
    for char in password:
        if char.islower():
            check_lower = True
        elif char.isupper():
            check_upper = True
        elif char.isdigit():
            check_digit = True
    if check_len and check_upper and check_lower and check_digit:
        return True
    return False



password = password_check()
print(password)