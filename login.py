def login(username, password):
    if username == "admin" and password == "admin123":
        print("Welcome admin!")
        return True
    print("Invalid credentials!")
    return False

print("Login System v2.0")
