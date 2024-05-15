def buy_choco(prices, money):
    sorted = list(filter(lambda x: x < money, prices))
    print(sorted)
    first_value = round(money / 2)
    second_value = money - first_value
    print(second_value)
    for i in sorted:
        if i <= first_value:
            first_value = i
            continue
        if i <= second_value:
            first_value += i
            break
    print(first_value)
    money -= first_value
    print(money)
    return money
