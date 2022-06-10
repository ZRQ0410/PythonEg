info = {
    1: {"name": "book", "price": 100},
    2: {"name": "phone", "price": 200},
    3: {"name": "tv", "price": 300},
    4: {"name": "food", "price": 400},
    5: {"name": "clothes", "price": 500}
}

cart = []


def print_info():
    for k, v in info.items():
        print("{}. {}: {}".format(k, v["name"], v["price"]))


def create_order():
    select = int(input("Choose the number: "))
    numbers = int(input("Enter the number of products: "))
    if cart:  # 如果购物车有东西
        for i in range(len(cart)):
            if info[select]["name"] == cart[i][0]["name"]:  # 如果已加入该商品
                cart[i][1] += numbers
                break
        else:
            cart.append([info[select], numbers])  # 如果未加入该商品
    else:  # 如果购物车空
        cart.append([info[select], numbers])
    print("Added to the cart.")


def shopping():
    print_info()
    create_order()


def print_order():
    print("You take:")
    for i in cart:
        print("\t{} {},  {}".format(i[1], i[0]["name"], i[0]["price"] * i[1]))


def calculate_price():
    total = 0
    for i in cart:
        total += i[0]["price"] * i[1]
    print("You need to pay {}.".format(total))
    print(total)
    paying(total)


def paying(total):
    try:
        paid = int(input("Enter the amount of money: "))
        if paid > total:
            payback = paid - total
            print("Thanks for shopping. You got {} back.".format(payback))
        elif paid == total:
            print("Thanks for shopping.")
        else:
            print("Payment failed. Please enter the correct amount of money.")
            paying(total)
    except:
        print("Please enter a number.")
        paying(total)


def settlement():
    print_order()
    calculate_price()


while True:
    choice = input("Enter 1: browsing, 2: paying. ")
    if choice == "1":
        shopping()
        print()
    elif choice == "2":
        print("--------Paying--------")
        settlement()
        break
    else:
        print("Error number. Please try again.")
