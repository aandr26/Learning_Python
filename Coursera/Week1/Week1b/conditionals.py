def greet(friend,money):
    if friend and (money > 20):
        print ("Hi!")
        money -= 20
    elif friend:
         print ("Hello")
    else:
        print ("Give me your money")
        money += 10
    return money

money = 20

money = greet(True, money)
print ("Money: ", money)


money = greet(False, money)
print ("Money: ", money)


money = greet(True, money)
print ("Money: ", money)
