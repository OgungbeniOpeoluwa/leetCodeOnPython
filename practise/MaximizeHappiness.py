def maximumHappinessSum(array: list, k):
    counter = 0
    for count in range(k):
        value = max(array)
        if value == 0:
            return counter
        counter += value
        array.remove(value)
        array = list(map(lambda x: reduce_array(x), array))
        print(array)
    return counter

def reduce_array(value):
    if value > 0:
        value -= 1
        return value
    return value


