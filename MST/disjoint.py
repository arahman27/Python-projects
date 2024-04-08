from setlist import SetList
# When a DisjointSet class is instantiated it is passed nothing and contains no sets. 
# It creates an empty Python dictionary which will be used to store the elements of the DisjointSet.
class DisjointSet:
    def __init__(self):
        self.pd = {}
        
# If element already exists within the Disjoint set, the function does nothing and returns false.

    def make_set(self, element):
        if element in self.pd:
            return False
# If element does not exist in the DisjointSet, this function will add it to the DisjointSet by
# creating a new SetList object containing only one node, with the element as only value in the SetList
# adding a new dictionary entry where element is the key and a reference to the node containing element as the value
# return true
        set_list = SetList()
        set_list.make_set(element)
        self.pd[element] = set_list.get_front()
        return True
    
# Function returns the representative of the set containining element.    
    def find_set(self, element):
        if element in self.pd:
            node = self.pd[element]
            return node.get_set().representative()
        else:
            return None

# This function returns the number of sets in the DisjointSet. Note that this is not the same as the number of elements. 
# You can start with 2 elements in unique sets and join them using the union_set() function.
    def get_num_sets(self):
        representatives = set()
        for node in self.pd.values():
            representatives.add(node.get_set().representative())
        count = 0
        for _ in representatives:
            count += 1
    
        return count

# This function returns the number of elements in the DisjointSet.
    def __len__(self):
        count = 0
        for _ in self.pd:
            count += 1
        return count

    
#This function returns the size of the set containing element. 
# If element does not exist within the disjoint set, function returns 0
    def get_set_size(self, element):
        if element not in self.pd:
            return 0

        node = self.pd[element]
        set_list = node.get_set()
        return len(set_list)

# Function performs a union of the two sets containing element1 and element2 respectively. 
# If the two elements are already in the same set or if either of the elements do not exist, 
# function does nothing and returns false. otherwise perform a union on the two sets, 
# creating one set and return true

    def union_set(self, element1, element2):
        if element1 not in self.pd or element2 not in self.pd:
            return False
        set1 = self.pd[element1].get_set()
        set2 = self.pd[element2].get_set()

        if set1 == set2:
            return False

        set1.union_set(set2)
        return True
    