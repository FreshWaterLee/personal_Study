import random

def select_sort(random_list):
	for i in range(0,len(random_list)-1):
		for j in range(i,len(random_list)):
			if random_list[i]>random_list[j]:
				temp = random_list[j]
				random_list[j]=random_list[i]
				random_list[i] = temp
	return random_list

if __name__=="__main__":
	list1 = []
	for i in range(5):
		list1.append(random.randint(1,15))
	print("before : ",list1)
	f_list = select_sort(list1)
	print("After",f_list)