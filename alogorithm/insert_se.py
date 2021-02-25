import random

def insert_se(my_list):
	for i in range(1,len(my_list)):
		ck_idx = i
		temp = my_list[i]
		while my_list[ck_idx-1] >temp:
			my_list[ck_idx]=my_list[ck_idx-1]
			ck_idx-=1
			if(ck_idx ==0):
				break
		my_list[ck_idx] = temp
		print(my_list)
		print()

if __name__ == '__main__':
	list1 = []
	while len(list1)<6:
		a = random.randint(1,15)
		if a in list1:
			print("Exist Number")
		else:
			list1.append(a)
	print("before : ",list1)
	insert_se(list1)