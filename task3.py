from bubblesort import bubbleSort




def testSort(sortMethod1, sortMethod2):

    array1 = [3, 4, 1, 2]
    array2 = [3.2, 0.01, 0.001, 4.3, 5]
    array3 = [-1, 4, 0, -0.4, 1.2]

    if (
        sortMethod1(array1) == sortMethod2(array1) and
        sortMethod1(array2) == sortMethod2(array2) and
        sortMethod1(array3) == sortMethod2(array3) 
    ):
        print('Result of two methods are identical.')
        return True
    else:
        print('Result of two methods are not identical!')
        return False


testSort(bubbleSort, sorted)