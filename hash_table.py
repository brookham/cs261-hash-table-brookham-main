# Hashtable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
#
# Name          : Brook Hamilton
# Collaborators : 
# Time spent    : 

class HashTable:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.dict = {}
        self.values = []

    def set_capacity(self, new_cap):
        self.capacity = new_cap

    def __setitem__(self, value, key):
        self.dict[key] = value

    def __getitem__(self, key):
        if key in self.dict:
            return self.dict[key]
        else: raise KeyError("Missing key")
    
    def hash(self, key):
        self.hash_value = hash(key) * (hash(key) + 3) % self.capacity
        return self.hash_value
        
