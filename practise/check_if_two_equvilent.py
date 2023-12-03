def string_equvilent_function(inputs: list, inputs_two: list):
    result = check_inputs(inputs)
    result2 = check_inputs(inputs_two)
    if result == result2:
        return True


def check_inputs(inputs: list):
    result = ""
    if len(inputs) >= 2:
        for count in inputs:
            result += count
    else:
        result += inputs.pop()
    return result
