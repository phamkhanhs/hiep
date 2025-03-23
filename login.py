def login(username, password):
    if username == "admin" and password == "feature1_password":
        print("Welcome to Feature 1!")
        return True
    print("Access denied in Feature 1!")
    return False

print("Login System - Feature 1 Version")