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
        self.values = [[] for _ in range(self.capacity)]
        self.len = 0


    def set_capacity(self, new_cap):
        self.capacity = new_cap
        self.values = [[] for _ in range(new_cap)]

    def __setitem__(self, key, value):
        index = self.hash(key)
        bucket = self.values[index] #location of inner array at index
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self.len += 1

    def __getitem__(self, key):
        index = self.hash(key)
        bucket = self.values[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        raise KeyError("Missing key")
    
    def hash(self, key):
        self.hash_value = hash(key) * (hash(key) + 3) % self.capacity
        return self.hash_value
    
    def delete(self, key):
        index = self.hash(key)
        bucket = self.values[index]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                self.len -= 1
                return
        raise KeyError("Missing key")

    def __len__(self):
        return self.len
    
    def clear(self):
        self.values = [[] for _ in range(self.capacity)]
        self.len = 0

    def keys(self):
        keys = []
        for bucket in self.values:
            for pair in bucket:
                keys.append(pair[0])
        return keys
    
    def vals(self):
        values = []
        for bucket in self.values:
            for pair in bucket:
                values.append(pair[1])
        return values