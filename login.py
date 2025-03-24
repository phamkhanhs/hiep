def login(username, password):
    if username == "admin" and password == "main_branch_2023":
        print("Welcome to Main System!")
        return True
    print("Access Denied - Main Branch!")
    return False

print("Login System v2.0")
