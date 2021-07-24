input = "abadabace"
alphabet_array = [0] * 26


def find_not_repeating_character(string):
    k = 0
    for char in string:
        if not char.isalpha():
            continue
        alphabet_array[ord(char) - ord("a")] += 1

    for i in string:
        if  alphabet_array[ord(i)-ord("a")]==1:
            return i

result = find_not_repeating_character(input)
print(result)