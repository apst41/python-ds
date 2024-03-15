def reverse_string(input_string):
    input_string = input_string[::-1]
    return input_string


if __name__ == '__main__':
    old_string = 'ajay'
    test_string = ''.join(sorted(old_string))
    print(old_string)
    print(test_string)
