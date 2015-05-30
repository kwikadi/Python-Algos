def bubbleSort(alist):
	for i in range(len(alist)):
		for j in range(len(alist)-i-1):
			if alist[j] > alist[j+1]:
				alist[j], alist[j+1] = alist[j+1], alist[j]

alist = [23,2,53,545,2,4,46,13,45,75]
bubbleSort(alist)
print(alist)

