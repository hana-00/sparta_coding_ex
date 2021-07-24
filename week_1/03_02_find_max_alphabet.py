input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    k = 0
    for char in string:
        if not char.isalpha():
            continue
        alphabet_occurrence_array[ord(char) - ord("a")] += 1
    for i in alphabet_occurrence_array:
        if alphabet_occurrence_array[i]>k:
            k=i
    return k


result = find_max_occurred_alphabet(input)
print(chr(result+97))



#input = "hello my name is sparta"

#def find_max_occurred_alphabet(string):
#    alphabet_array=["a","b","c","d","e","f","g","h","i","j","k","l,"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#    max_alphabet = alphabet_array[0]
#    max_occurrance = 0
#    for alphabet in alphabet_array
#        occurance =0
#        for char in string:
#           if char == alphabet:
#                occurance += 1
#        if accurrance > max_occurrance:
#            max_occurrance = occurrance
#            mac_alphabet = alphabet
#        return max_alphabet

#result = find_max_occurred_alphabet(input)
#print(result)