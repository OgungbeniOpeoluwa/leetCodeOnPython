def return_even_and_odd_in_zero_and_one(inputs):
    result = list(map(lambda x: filter_result(x), inputs))
    return result


def filter_result(value):
    if value % 2 == 0:
        return False
    return True
