def sortedSquaredArray(array):
    newArray = []
    index = 0

    for number in array:
        newArray.append(number*number)
        index = index + 1
    
    newArray.sort()
    return newArray

print(sortedSquaredArray([-2,-1]))