def insertionSort( aList ):
    for i in range(1, len(aList)):
        temp = aList[i]
        k = i
        while k > 0 and temp < aList[k - 1]:
            aList[k] = aList[k - 1]
            k -= 1
        aList[k] = temp
        
alist = [3,24,34,2,65,5,54,3,7,6]
insertionSort(alist)
