#You are given a string S.
#Your task is to find out if the string s contains: alphanumeric characters, alphabetical characters, 
#digits, lowercase and uppercase characters.

if __name__ == '__main__':
    myString = input()
    
    digitCount = 0
    islowerCount = 0
    isUpperCount = 0
    isAlphaNum   = 0
    isAlphaCount = 0

    #check if contains any digit in the string
    for items in myString:
        if items.isdigit():
            digitCount += 1 
        if items.islower():
            islowerCount += 1
        if items.isupper():
            isUpperCount += 1
        if items.isalpha():
            isAlphaCount += 1
        if items.isalnum():
            isAlphaNum += 1

    if isAlphaNum > 0:
        print(True)
    if isAlphaNum <= 0:
        print(False)
    
    if isAlphaCount > 0:
        print(True)
    if isAlphaCount <= 0:
        print(False)

    if digitCount > 0:
        print(True)
    if digitCount <= 0:
        print(False)
    
    if islowerCount > 0:
        print(True)
    if islowerCount <= 0:
        print(False)
    
    if isUpperCount > 0:
        print(True)
    if isUpperCount <= 0:
        print(False)
