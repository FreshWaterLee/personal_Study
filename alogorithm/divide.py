import random

def mergel(rlist):
	if len(rlist) <2:
		return rlist
	mid = len(rlist)//2
	left = rlist[:mid]
	right = rlist[mid:]
	print("left ",left)
	print("right ",right)
	left = mergel(left)
	right = mergel(right)
	result = []
	while len(left)>0 or len(right)>0:
		if len(left) > 0 and len(right)>0:
			if left[0]<=right[0]:
				result.append(left[0])
				left = left[1:]
			else:
				result.append(right[0])
				right = right[1:]
		elif len(left)>0:
			result.append(left[0])
			left = left[1:]
		elif len(right)>0:
			result.append(right[0])
			right= right[1:]
	print('result ',result)
	return result
if __name__ == '__main__':
	list1 = []
	for i in range(20):
		list1.append(random.randint(1,20))
	#print(merge_sort(list1))
	print(mergel(list1))