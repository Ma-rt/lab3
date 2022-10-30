# O(3log(n)) => O(log(n))
def is_value_exist(values, required_value):
    middle = len(values) // 2
    low = 0
    high = len(values) - 1

    while values[middle] != required_value and low <= high:
        if required_value > values[middle]:
            low = middle + 1
        else:
            high = middle - 1
        middle = (low + high) // 2
    return values[middle] == required_value


# O(nlogn)
def check_required_values_existing(values, required_values):
    result = []
    for i in range(len(values)):
        result.append(is_value_exist(values, required_values[i]))

    return result