def combinations(arr, r):
    result = []
    _combinations(arr, r, 0, [], result)
    return result

def _combinations(arr, r, start, current_combination, result):
    if len(current_combination) == r:
        result.append(current_combination)
        return
    if start >= len(arr):
        return
    _combinations(arr, r, start + 1, current_combination + [arr[start]], result)
    _combinations(arr, r, start + 1, current_combination, result)
arr = [1, 2, 3, 4]
r = 3
result = combinations(arr, r)
print(result)
