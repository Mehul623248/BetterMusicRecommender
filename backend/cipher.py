def encrypt(inputText: str, N: int, D: int) -> str:
    if not (verifyInput(inputText, N, D)):
        return None
    inputText = inputText[::-1]
    charList = list(inputText)
    for i in range(len(charList)):
        char = ord(charList[i])
        if (D > 0):
            char += N
        else:
            char -= N
        while (char < 34):
            char += 92
        while (char > 126):
            char -= 92
        charList[i] = chr(char)
    return "".join(charList)


def decrypt(inputText: str, N: int, D: int) -> str:
    if not (verifyInput(inputText, N, D)):
        return None
    inputText = inputText[::-1]
    charList = list(inputText)
    for i in range(len(charList)):
        char = ord(charList[i])
        if (D < 0):
            char += N
        else:
            char -= N
        while (char < 34):
            char += 92
        while (char > 126):
            char -= 92
        charList[i] = chr(char)
    return "".join(charList)


def verifyInput(inputText: str, N: int, D: int) -> bool:
    validIn = True
    if inputText is None:
        print("NoneType not allowed")
        return False
    for char in inputText:
        if not (34 <= ord(char) <= 126):
            print("Input can only contain ASCII printable characters except for space and '!'")
            validIn = False
            break
    if (N < 1):
        print("N must be >= 1")
        validIn = False
    if ((D != 1) & (D != -1)):
        print("D can only be 1 or -1")
        validIn = False
    return validIn