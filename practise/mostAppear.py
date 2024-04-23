def returnMostAppear(input: list):
    counts = 0
    number = 0
    for value in input:
        result = input.count(value)
        if result > counts:
            counts = result
            number = value
    return number
