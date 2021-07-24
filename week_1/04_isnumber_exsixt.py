input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for i in array: #array의 길이만큼 아래 반복 실행
        if i == number: #비교연산 1번
            return True #N+1만큼
    return False


result = is_number_exist(3, input)
print(result)