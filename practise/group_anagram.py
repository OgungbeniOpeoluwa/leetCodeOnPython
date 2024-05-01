from collections import Counter


def groupAnagrams(value):
    results = []
    for result in value:
        if checkIfValueAlreadyExistInList(result, results):
            continue
        return_list = checkIfAnagramExist(value, result)
        results.append(return_list)
    return results


def checkIfValueAlreadyExistInList(value, lists):
    for first_value in lists:
        for second_value in first_value:
            if second_value == value:
                return True
    return False


def checkIfAnagramExist(values, each_value: str):
    lists = []
    for result in values:
        numb = Counter(each_value)
        r = Counter(result)
        if numb == r:
            lists.append(result)
    return lists
