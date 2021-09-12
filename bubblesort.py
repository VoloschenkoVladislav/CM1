def bubbleSort(array, reverse = False):

    compare = (lambda x, y: x < y) if not reverse else (lambda x, y: x > y) 

    for i in range( len(array) - 2 ):
        for j in range( len(array) - 1 ):
            x, y = array[j], array[j + 1]
            if not compare(x, y):
                array[j + 1], array[j] = x, y

    return array