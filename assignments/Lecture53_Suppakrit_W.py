def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice * 7 / 100)
    return result

totalPrice = int(input("Input your total price: "))
print(vatCalculate(totalPrice))