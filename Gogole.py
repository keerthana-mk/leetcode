def maxNumber(number):
    maxNum = number
    numberString = list(str(number))
    print(numberString)
    # count, total = 0, 0
    for i in range(len(numberString)):
        j = i + 1
        maxTillNow = numberString[i]
        while j < len(numberString):
            total += 1
            if numberString[j] > numberString[i] and numberString[j] >= maxTillNow:
                count += 1
                maxTillNow = numberString[j]
                newNum = int(''.join(numberString[:i] + numberString[i:j + 1][::-1] + numberString[j + 1:]))
                if newNum > maxNum:
                    maxNum = newNum
            j += 1
    print('number of computations: {}/{}'.format(count, total))
    print('maxNumber obtained for {} is {}'.format(number, maxNum))

# def maxNumberV2(number):
#     maxNum = number
#     numberString = list(str(number))
#     i, j = 0, 0
#     while i <= j and j < len(numberString):
#         if i == j:
#             j += 1
#         elif numberString[i] < numberString[j]:
#             j += 1
#         else:
#             newNumber = ''.join(numberString[:i] + numberString[i:j][::-1] + numberString[j:])
#             if maxNum < int(newNumber):
#                 maxNum = int(newNumber)
#             i = j
#     return maxNum

if __name__ == "main":
    inputList = [5340, 2043, 602, 1356, 1080, 123456, 988868, 5235]
    for input in inputList:
        print('for {}, maxNum is {}'.format(input, maxNumber(input)))