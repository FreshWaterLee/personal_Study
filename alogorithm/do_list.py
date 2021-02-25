class Node:
	def __init__(self,data,bef=None,nex=None):
		self.data = data
		self.bef = bef
		self.nex = nex
def init_list():
	global node_A
	node_A = Node('A')
	node_B = Node('B')
	node_D = Node('D')
	node_F = Node('F')
	node_A.nex = node_B
	node_B.nex = node_D
	node_B.bef = node_A
	node_D.nex = node_F
	node_D.bef = node_B
	node_F.bef = node_D
def print_list():
	global node_A
	node = node_A
	while node:
		print(node.data)
		node = node.nex
	print()
def insert_list(data):
	global node_A
	new_no = Node(data)
	node_b = node_A
	node_n = node_A
	while node_n.data <= data:
		node_b = node_n
		node_n = node_n.nex
	new_no.nex = node_n
	node_b.nex = new_no
	new_no.bef = node_b
	node_n.bef = new_no

def delete_node(del_data):
	global node_A
	pre_node = node_A
	next_node = pre_node.nex
	next_next_node = next_node.nex

	if pre_node.data == del_data:
		node_A = next_node
		del pre_node
		return
	while next_node:
		if next_node.data == del_data:
			next_next_node = next_node.nex
			pre_node.nex = next_node.nex
			next_next_node.bef = next_node.bef
			break
		pre_node = next_node
		next_node = next_node.nex
		next_next_node = next_node.nex


if __name__ == '__main__':
	print("2D Chain List!!")
	init_list()
	insert_list('C')
	print_list()
	delete_node('C')
	print_list()