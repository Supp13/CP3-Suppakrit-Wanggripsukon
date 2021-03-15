usernameInput = input("Username : ")
passwordInput = input("Password : ")
while usernameInput != "admin" or passwordInput != "1234":
    print("The user name or password is incorrect")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
print("Done !")