def reverse_string(input_string):
    input_string = input_string[::-1]
    return input_string


def allSubString(input_string):
    if len(input_string) == 0:
        return
    
    print(input_string)
    
    allSubString(input_string[1:])
    allSubString(input_string[:-1])


if __name__ == '__main__':
    allSubString('abc')
