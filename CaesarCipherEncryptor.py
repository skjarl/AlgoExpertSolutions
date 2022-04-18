def ceasarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    
    if newLetterCode <= 122:
        code = chr(newLetterCode)
    else:
        code = chr(96 + newLetterCode % 122)
    return code

print(ceasarCipherEncryptor("ayx", 2))