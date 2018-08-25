def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    #create mapping of digit to leters 
    digToLet = {}
    digToLet["2"] = "abc"
    digToLet["3"] = "def"
    digToLet["4"] = "ghi"
    digToLet["5"] = "jkl"
    digToLet["6"] = "mno"
    digToLet["7"] = "pqrs"
    digToLet["8"] = "tuv"
    digToLet["9"] = "wxyz"
    sizeList = 1
    for i in digits:
        if i == '7' or i == '9':
            sizeList = sizeList * 4
        else:
            sizeList = sizeList * 3
    result = []
    sizeFirst = len(digToLet[digits[0]])
    i = 0
    while i < sizeList:
        result.append(digToLet[digits[0]][i%sizeFirst])
        i = i + 1 
    for i in digToLet[digits[1:]]:
        for j in result:
            j.append(i)
    return result
def main():
    letterCombinations("23")

if __name__ == "__main__":
    main()
