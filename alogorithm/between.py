def between(x,start,ranges):
	for target in range(start+ranges,len(x),ranges):
		val = x[target]
		i = target
		while i> start:
			if x[i - ranges] > val:
				x[i] = x[i-ranges]
			else:
				break
			i -= ranges
		x[i] = val

def shellsort(x):
	ranges = len(x)//2
	while ranges >0:
		for start in range(ranges):
			between(x,start,ranges)
		ranges = ranges//2

x = [5,2,8,6,1,9,3,7]
shellsort(x)
print(x)