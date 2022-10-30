# O(3n) => O(n)
def is_unique(values):
    value_set = set(values)
    return len(value_set) == len(values)