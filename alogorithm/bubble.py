def bubble(my_list):
	for st_idx in range(len(my_list)-1):
		for j in range(1, len(my_list)-st_idx):
			if(my_list[j]<my_list[j-1]):
				temp = my_list[j-1]
				my_list[j-1] = my_list[j]
				my_list[j] = temp


if __name__ == '__main__':
	list1 = [5,3,1,2,4]
	bubble(list1)
	print(list1)