usernameInput = input("Username : ")
passwordInput = input("Password : ")
print('-'*40)
if usernameInput == "Khiem" and passwordInput == "123":
    print("Welcome to Emmee Shop")
    print("Product List")
    print("1. Pen    10 baht")
    print("2. Pencil 15 baht")
    print("3. Eraser 20 baht")
    print("4. Ruler  25 baht")
    userSelected = int(input("Order of products (1/2/3/4): "))
    if userSelected == 1:
        amount = int(input("Amount: "))
        print('-' * 40)
        print(f'Total : {10*amount} baht')
    elif userSelected == 2:
        amount = int(input("Amount: "))
        print('-' * 40)
        print(f'Total : {15 * amount} baht')
    elif userSelected == 3:
        amount = int(input("Amount: "))
        print('-' * 40)
        print(f'Total : {20 * amount} baht')
    elif userSelected == 4:
        amount = int(input("Amount: "))
        print('-' * 40)
        print(f'Total : {25 * amount} baht')
    else:
        print("Sorry, we don't have that product.")
    print("Thank you for Shopping with us")
else:
    print('Your username or password is wrong')
    print('Please try again')