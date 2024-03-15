def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def factorial(a):
    if a == 0:
        return 1
    return a * factorial(a - 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(factorial(5))
