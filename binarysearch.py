def binarySearch(search, val):
	first = 0
	last = len(search)-1
	found = False
	while first<=last:
		mid = (first + last)//2
		if search[mid] == val:
			print "Found at index" + str(mid)
			return
		else:
			if val < search[mid]:
				last = mid-1
			else:
				first = mid+1
	print "Number not found"
	
testlist = [0,1,2,3,4,5,6,7,8,9]
binarySearch(testlist, int(raw_input("Enter the number to search:")))