def radix(order):
	is_sorted = False
	pos = 1

	while not is_sorted:
		is_sorted =True
		queue_list = [list() for _ in range(10)]

		for num in order:
			dig_num = (int) (num/pos) %10
			queue_list[dig_num].append(num)
			if is_sorted and dig_num >0:
				is_sorted = False
		index = 0

		for numbers in queue_list:
			for num in numbers:
				order[index] = num
				index +=1
		pos *=10

ordee = [10,5,7,4,1,2,9,8,3,6]
print(ordee)
radix(ordee)
print(ordee)