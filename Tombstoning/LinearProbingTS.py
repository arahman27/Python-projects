class LinearProbingTS:

	# This is a single record in a chaining hash table.  You can
	# change this in anyway you wish (including not using it at all)
	class Record:
		def __init__(self, key = None, value=None, status=None):
			self.key = key
			self.value = value
			self.status = status

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use chaining for collision resolution)

	def __init__(self, cap=32):
		self.cap = cap
		self.length = 0
		self.tbl = [None] * self.cap

	#Inserts a new key-value pair Record into the table if the key does not already exists
	#Returns True if key-value pair added, False if key-value pair already exists
	def insert(self,key, value):
		hash_idx = hash(key) % self.capacity()

		#If the key already exists in the table then return false as no insertion will be made
		while self.tbl[hash_idx] is not None:
			if self.tbl[hash_idx].key == key and self.tbl[hash_idx].status == "O":
				return False
			
			hash_idx = (hash_idx + 1) % self.capacity()
			
			if hash_idx == self.capacity() - 1:
				hash_idx = 0
		
		#Marking the spot "O" for occupied and adding the Record to the table
		self.tbl[hash_idx] = self.Record(key, value, "O")
		self.length = self.length + 1

		#Test load factor and if it exceeds 0.7 then perform expansion of the table
		if (len(self)/ self.capacity()) > 0.7:
			new_table = LinearProbingTS(self.capacity() * 2)

			for record in self.tbl:
				if record is not None:
					new_table.insert(record.key, record.value)

			self.tbl = new_table.tbl
			self.cap = new_table.cap

		return True

	#Helper function: Search for the given key and return the index of the Record where the key was found
	def search_index(self, key):
		hash_idx = hash(key) % self.capacity()

		#Keep searching until first element that is empty and only return the matching key if it is occupying in the table.
		while self.tbl[hash_idx] is not None:
			if self.tbl[hash_idx].key == key and self.tbl[hash_idx].status == "O":
				return hash_idx
			
			hash_idx = (hash_idx + 1) % self.capacity()
			
			if hash_idx == self.capacity() - 1:
				hash_idx = 0
		
		return None

	#Set the key-value pair for the Record with matching key to the given key-value pair and return True. Returns False if no matching key was found.
	def modify(self, key, value):
		hash_idx = self.search_index(key)

		if hash_idx is None:
			return False
		else:
			self.tbl[hash_idx].key = key
			self.tbl[hash_idx].value = value
			return True
	
	#Set the status of the record with matching key to "X" for deleted and return True. Otherwise, return False if no matching key was found.
	def remove(self, key):
		hash_idx = self.search_index(key)

		if hash_idx is None:
			return False
		else:
			self.tbl[hash_idx].status = "X"
			self.length = self.length - 1
			return True

	#Search for the given key using search_index() and return the index of the Record where the key was found.
	def search(self, key):
		idx = self.search_index(key)
		
		if idx is not None:
			return self.tbl[idx].value

		return None

	#Returns the capacity of the table.
	def capacity(self):
		return self.cap
	
	#Returns the length of the table based on the number of occupied/used Records currently in the table.
	def __len__(self):
		return self.length