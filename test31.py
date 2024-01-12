def password_check():
    password = input("Введите пороль: от 10 символов ")
    check_len = False
    check_upper = False
    check_lower = False
    check_digit = False

    if len(password) >= 10:
        check_len = True
    if password.isupper() == False:
        check_upper = True
    if password.islower() == False:
        check_lower = True
    if password.isdigit() == False:
        check_digit = True
    if check_len and check_upper and check_lower and check_digit == True:
        return True
    else:
        return False



password = password_check()
print(password)
