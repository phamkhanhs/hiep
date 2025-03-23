def login(username, password):
    if username == "admin" and password == "main_password":
        print("Welcome to Main Branch!")
        return True
    print("Access denied in Main!")
    return False

print("Login System - Main Version")