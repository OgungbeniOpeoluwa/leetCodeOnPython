def return_diffrences(number, key):
    divisible = 0
    non_divisible = 0
    for numb in range(1, (number + 1)):
        if numb % key == 0:
            divisible += numb
        else:
            non_divisible += numb
    return non_divisible - divisible
