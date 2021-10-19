def upcCheckDigit(upcStr):
    upcStr = str(upcStr)
    if len(upcStr) != 12:
        raise Exception("Invalid length")

    oddSum = 0
    evenSum = 0
    for i, char in enumerate(upcStr):
        j = i+1
        if j % 2 == 0:
            evenSum += int(char)
        else:
            oddSum += int(char)
            totalSum = (evenSum * 3) + oddSum
            mod = totalSum % 10
            checkDigit = 10 - mod
        if checkDigit == 10:
            checkDigit = 0
    return upcStr + str(checkDigit)


def bcCheckDigit(bcStr):
    bcStr = str(bcStr)
    for i, char in enumerate(bcStr):
        totalSum = bcStr
        mod = totalSum % 10
        checkDigit = 10 - mod
    if 0 <= checkDigit <= 9:
        return bcStr + str(checkDigit)


def pcCheckDigit(pcStr):
    pcStr = str(pcStr)
    for i, char in enumerate(pcStr):
        totalSum = pcStr
        mod = totalSum % 10
        checkDigit = 10 - mod
    return pcStr + str(checkDigit)
