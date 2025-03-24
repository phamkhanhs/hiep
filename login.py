def login(username, password):
    if username == "admin" and password == "feature2_secret":
        print("Welcome to Feature 2!")
        return True
    print("Access Denied - Feature 2!")
    return False

print("Login System - Feature 2 Edition")
print("Version 3.0")
