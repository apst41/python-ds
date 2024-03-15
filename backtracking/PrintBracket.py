def printBracket(count):
    printHelper('', 0, 0, count)


def printHelper(current, lCount, rCount, count):
    if len(current) == count * 2:
        print(current)
        return
    
    if lCount < count:
        printHelper(current + '(', lCount + 1, rCount, count)
    
    if rCount < lCount:
        printHelper(current + ')', lCount, rCount + 1, count)


if __name__ == '__main__':
    printBracket(3)
