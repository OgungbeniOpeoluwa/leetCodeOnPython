def buy_choco(prices, money):
    sorted = list(filter(lambda x: x < money, prices))
    if len(sorted) == 0:
        return money
    first_value = 0
    for i in range(0, len(sorted)):
        for a in range(0 + i, len(sorted)):
            if i + a <= money:
                first_value = i+a
                return first_value
    money -= first_value
    return money
