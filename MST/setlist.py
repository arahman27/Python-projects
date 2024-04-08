class SetList:
	class Node:
		#Constructor to create a Node object with the passed data and SetList reference. References to next and previous Node objects are optional, set to None by default.
		def __init__(self,data,set_list,next_node = None,prev_node = None):
			self.data = data
			self.set_list = set_list
			self.next_node = next_node
			self.prev_node = prev_node

		#Returns the stored data value in the Node.
		def get_data(self):
			return self.data

		#Returns the reference to the next Node object in the list.
		def get_next(self):
			return self.next_node

		#Returns the reference to the previous Node object in the list.
		def get_previous(self):
			return self.prev_node

		#Returns the reference of the SetList object which holds this Node.
		def get_set(self):
			return self.set_list

	#Initializes the SetList object. On creation, the SetList is empty by setting the front and back Node to None.
	def __init__(self):
		self.front = None
		self.back = None

	#Returns the reference to the Node at the front of the list.
	def get_front(self):
		return self.front

	#Returns the reference to the Node at the back of the list.
	def get_back(self):
		return self.back

	#Uses the passed data to create a new Node object which is used to set front and back reference of this SetList. If the SetList is already created then return None as nothing new created. 
	def make_set(self, data):
		if self.front is None:
			new_node = self.Node(data, self)
			self.front = new_node
			self.back = new_node

			return new_node
		else:
			return None

	#Searches the SetList to find the Node with the passed data, starts the search from the front Node. Returns the Node with matching data if found otherwise returns None.
	def find_data(self, data):
		if self.front.get_data() == data:
			return self.front
		
		find_node = self.front

		while find_node is not None:
			if find_node.get_data() is data:
				return find_node
			
			find_node = find_node.next_node

		return None

	#Returns the representative Node of the list which is the front Node.
	def representative_node(self):
		if len(self) == 0:
			return None
		else:
			return self.front

	#Returns the data value stored within the representative Node.
	def representative(self):
		if len(self) == 0:
			return None
		else:
			return self.front.get_data()

	#Joins the passed SetList with this SetList by transferring the elements of the passed set to this one. Returns the number of elements transferred.
	def union_set(self, other_set):
		count = 0
		node = self.pop_node(other_set)

		while node is not None:
			if self.front is None:
				self.front = node
				self.back = node
				node.set_list = self
				count += 1
			else:
				node.set_list = self
				node.prev_node = self.back
				self.back.next_node = node
				self.back = node
				count += 1

			node = self.pop_node(other_set)

		other_set.front = None
		other_set.back = None

		return count

	#Returns the number of Node elements in this SetList
	def __len__(self):
		count = 0

		if self.front is None:
			return count
		else:
			node = self.front

			while node is not None:
				node = node.get_next()
				count += 1
			
			return count

	#Helper function for union_set. Returns front node front other_set and rearranges other_set for next node.
	def pop_node(self, other_set):
		node = None

		if other_set.front is None:
			return node
		elif other_set.front.next_node is None:
			node = other_set.front
			other_set.front = None
			return node
		else:
			node = other_set.front
			other_set.front = other_set.front.next_node
			other_set.front.prev_node = None
			return node

