def selectionSort(alist):
	for i in range(len(alist)):
		max = 0 # Note: will only work for lists with positive numbers
		indx = i
		for j in range(i,len(alist)):
			if alist[j] > max:
				max = alist[j]
				indx = j
		alist[indx], alist[i] = alist[i], alist[indx]
	print(alist)

alist = [3,24,34,2,65,5,54,3,7,6]
selectionSort(alist)

# Decreasing this time, for fun