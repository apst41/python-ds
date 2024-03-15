if __name__ == '__main__':
    my_set = set()
    for i in range(1, 10):
        my_set.add(i)
    
    print(my_set)
    
    for i in range(0, 100):
        my_set.add(i)
    print(my_set)
    
    if -1 in my_set:
        print('hello')
