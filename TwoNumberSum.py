# def twoNumberSum(array, targetSum):
#     for firstNumber in array:
#         for secondNumber in array:
#             if secondNumber != firstNumber:
#                 if firstNumber + secondNumber == targetSum:
#                     return [firstNumber,secondNumber]
#     return []

def twoNumberSum(array, targetSum):
    numberHashTable = {}
    
    for number in array:
        calculatedAnswer = targetSum - number
        if calculatedAnswer in numberHashTable:
            return [number,calculatedAnswer]
        else:
            numberHashTable[number] = True
            
    return []

array = [3,5,-4,8,11,1,-1,6]
targetSum = 19
print(twoNumberSum(array, targetSum))