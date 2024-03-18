from sortedcontainers import SortedSet


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
    my_set = SortedSet()
    
    my_set.add('a')
    my_set.add('b')
    my_set.add('c')
    my_set.add('d')
    my_set.add('e')
    
    while my_set:
        print(my_set.pop())
