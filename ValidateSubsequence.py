def isValidSubsequence(array, sequence):
    
    index = 0

    for number in array:
        if index > len(sequence):
            return False
        if number == sequence[index]:
            index = index + 1
            if index > len(sequence):
                return True
        else:
            if index > len(sequence):
                return False
    
    return True

input = [5, 1, 22, 25, 6, -1, 8, 10]
seq = [22, 25, 6]
print (isValidSubsequence(input, seq))