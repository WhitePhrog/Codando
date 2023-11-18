def check_register(msg, lenght, type_):
    checking = input(msg)
    if len(checking) < lenght:
        print(f"{type_} too small. It must be at least {lenght} characters.")
        return check_register(msg, lenght, type_)
    else:
        print(f"Great! Your {type_} will be: {checking}")
        return checking


username = check_register("Welcome to our registration system, please choose an username: ", 8, "username")
password = check_register("Now please, choose a password: ", 10, "password")
print("Excelent! You are now registered under the following data.\n"
      f"Username: {username}\n"
      f"Password: {password}")
