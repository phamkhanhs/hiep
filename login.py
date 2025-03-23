def login(username, password):
    if username == "admin" and password == "feature1_password":
        print("Welcome to Feature 1!")
        return True
    print("Invalid credentials!")
    return False

print("Login System v2.0")
