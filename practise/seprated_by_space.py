def return_seprated_string(input1: str, input2: str):
    result = input2[0:2]+input1[2:]
    result2 = input1[0:2]+input2[2:]
    return f"{result } {result2}"
