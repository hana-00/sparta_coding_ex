input = [0, 3, 5, 6, 1, 2, 4]

#0과 1은 더하는게 더 크다
def find_max_plus_or_multiply(array):
    result = 0
    for i in array:
        if (i <= 1) or result <= 1:
            result = result + i
        else:
            result = result * i
    return result


result = find_max_plus_or_multiply(input)
print(result)