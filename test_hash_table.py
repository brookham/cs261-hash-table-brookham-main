# DO NOT MODIFY THE TESTS IN THIS FILE
# Run me via: python3 -m unittest test_hash_table or
# py -m unittest test_hash_table

import unittest
import time
import random
from hash_table import HashTable


class TestHashTable(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        Test 1: A HashTable exists.
        """
        try:
            HashTable()
        except NameError:
            self.fail("Could not instantiate HashTable.")

    def test_size(self):
        """
        Test 2: A default HashTable has a size attribute that is 100.
        """
        h = HashTable()
        self.assertEqual(100, h.capacity)

    def test_instantiation_with_size(self):
        """
        Test 3: A HashTable can be instantiated with an optional size.
        """
        h = HashTable(25)
        self.assertEqual(25, h.capacity)

    """
    Basic API
    """
    #Hint: Do the naive thing. You do NOT need data storage to pass this test.
    def test_simple_insertion(self):
        """
        Test 4: Insert a single key-value pair into to hash table
        """
        h = HashTable()
        try:
            h['spam'] = 'eggs'
        except TypeError:
            self.fail("HashTable has no __setitem__ implementation")

    #Hint: Do the naive thing. You do NOT need data storage to pass this test.
    def test_simple_retrieval(self):
        """
        Test 5: Retrive a value from the hash table. If key not present, raise KeyError
        """
        h = HashTable()
        try:
            _ = h['spam']
            self.fail("Did not raise KeyError: Missing key.")
        except KeyError:
            pass
   
    def test_hash(self):
        """
        Test 6: Hash function uses the Knuth Variant on Division to distribute
        key-value pairs in the hash table. 
        Knuth Variant on Division : h(k) = k(k+3) mod m
        where k is the key and m is the number of "slots or buckets" in the hash table

        returns hash no greater than its size - 1.
        """
        h = HashTable(25)
        self.assertEqual(0, h.hash(0))
        self.assertEqual(5, h.hash(10))
        self.assertEqual(20, h.hash(15))
        self.assertEqual(10, h.hash(27))
        self.assertEqual(hash("fake key")*(hash("fake key")+3) % 25, h.hash("fake key"))

    """
    Data Storage
    """

    def test_data(self):
        """
        Test 7: A HashTable has an internal array for storing k-v pairs.
        """
        h = HashTable(50)
        self.assertEqual(list, type(h.values))

    # def test_data_contents(self):
    #     """
    #     Test 8: A HashTable data array contains empty lists.
    #     We need lists at each location in the array to store multiple 
    #     key-value pairs in the event of collisions
    #     """
    #     h = HashTable(5)
    #     expected = [ [], [], [], [], [] ]
    #     self.assertEqual(expected, h.values)

#     # """
#     # Insertion Basics
#     # """

#     def test_insert_one(self):
#         """
#         Test 9: Inserting a k-v pair stores it as a two-element array in the list at
#         the right index.
#         """
#         h = HashTable(5)
#         h[11] = 'eggs' # 11 is the key, not an index :)
#         self.assertEqual([[11, 'eggs']], h.values[4])

#     # """
#     # Retrieval Basics
#     # """

#     def test_retrieve_one(self):
#         """
#         Test 10: The value of an inserted k-v pair is retrievable.
#         """
#         h = HashTable(5)
#         h['spam'] = 'eggs'
#         self.assertEqual('eggs', h['spam'])

#     # """
#     # Insertion
#     # """

#     def test_insert_two(self):
#         """
#         Test 11: Inserting two k-v pairs stores them as two-element arrays in the list
#         at the right index.
#         """
#         h = HashTable(5)
#         h[9] = 'spam' # Using numbers as keys for visibility.
#         h[11] = 'eggs'
#         self.assertEqual([[9, 'spam']], h.values[3])
#         self.assertEqual([[11, 'eggs']], h.values[4])

#     def test_insert_existing(self):
#         """
#         Test 12: Inserting a k-v pair where the key already exists overwrites the old value.
#         """
#         h = HashTable(5)
#         h[9] = 'spam' # Using numbers as keys for visibility.
#         h[9] = 'eggs'
#         self.assertEqual([[9, 'eggs']], h.values[3])

#     def test_insert_collision(self):
#         """
#         Test 13: Inserting a k-v pair where the key has the same hash as an existing key
#         appends the new k-v pair to the list at the appropriate index.
#         """
#         h = HashTable(5)
#         h[9] = 'spam'
#         h[4] = 'eggs'
#         self.assertEqual([[9, 'spam'], [4, 'eggs']], h.values[3])

#     # """
#     # Deletion
#     # """

#     def test_delete(self):
#         """
#         Test 14: Deleting a key removes the k-v pair from the hash table.
#         """
#         h = HashTable(5)
#         h['spam'] = 'eggs'
#         h.delete('spam')
#         try:
#             _ = h['spam']
#             self.fail("Did not raise KeyError: Missing key.")
#         except KeyError:
#             pass
    
#     # """
#     # Hash table length
#     # """
#     def test_hash_table_length_empty(self):
#         """
#         Test 15: An empty hash table returns a length of 0
#         """
#         h = HashTable(5)
#         self.assertEqual(0, len(h))

#     def test_hash_table_length(self):
#         """
#         Test 16: An non-empty hash table returns the number of key-value pairs in the hash table
#         """
#         h = HashTable(50)
#         for key in range(75):
#             h[key] = fake_value()
#         self.assertEqual(75, len(h))
    
#     # """
#     # Misc. Methods
#     # """

#     def test_clear(self):
#         """
#         Test 17:A cleared HashTable has an empty data array.
#         """
#         h = HashTable(5)
#         h['spam'] = 'eggs'
#         h['needle'] = 'haystack'
#         h['osu'] = 'beavers'
#         h.clear()
#         self.assertEqual([[], [], [], [], []], h.values)

#     def test_initial_keys(self):
#         """
#         Test 18: A HashTable initially has no keys.
#         """
#         h = HashTable()
#         self.assertEqual([], h.keys())

#     def test_keys(self):
#         """
#         Test 19: A HashTable can produce a list of its keys.
#         """
#         h = HashTable()
#         h['spam'] = 'eggs'
#         h['osu'] = 'beavers'
#         h['needle'] = 'haystack'
#         keys = h.keys()
#         keys.sort()
#         self.assertEqual(['needle', 'osu', 'spam'], keys)

#     def test_initial_values(self):
#         """
#         Test 20: A HashTable initially has no values.
#         """
#         h = HashTable(5)
#         self.assertEqual([], h.vals())

#     def test_values(self):
#         """
#         Test 21: A HashTable can produce a list of its values.
#         """
#         h = HashTable()
#         h['spam'] = 'eggs'
#         h['osu'] = 'beavers'
#         h['needle'] = 'haystack'
#         values = h.vals()
#         values.sort()
#         self.assertEqual(['beavers', 'eggs', 'haystack'], values)

#     # """
#     # Time complexity
#     # """

#     def test_retrieval_is_constant_time(self):
#         """
#         Test 22: Retrieving a value from a dictionary should take the same amount of time
#         no matter how many k-v pairs it contains. It should be O(... what?)
#         """
#         time_samples = []
#         key = fake_key()
#         value = fake_value()
#         small_table = HashTable()
#         small_table[key] = value
#         large_table = HashTable(20000)
#         for _ in range(10000):
#             large_table[fake_key()] = fake_value()
#         large_table[key] = value
#         for _ in range(9999):
#             large_table[fake_key()] = fake_value()
#         small_average_elapsed_time = average_retrieval_time(small_table, key)
#         large_average_elapsed_time = average_retrieval_time(large_table, key)
#         self.assertAlmostEqual(small_average_elapsed_time, large_average_elapsed_time, delta=(small_average_elapsed_time+1e-6)*2)

#     def test_constant_retrieval_order(self):
#         """
#         Test 23: Retrieving a value using the first-used key and the most recently-used
#         key should be in constant time.
#         """
#         h = HashTable(20000)
#         first_key = fake_key()
#         last_key = fake_key()
#         h[first_key] = fake_value()
#         for _ in range(19998):
#             h[fake_key()] = fake_value()
#         h[last_key] = fake_value()
#         first_key_value_average_retrieval_time = average_retrieval_time(h, first_key)
#         last_key_value_average_retrieval_time = average_retrieval_time(h, last_key)
#         self.assertAlmostEqual(first_key_value_average_retrieval_time,\
#             last_key_value_average_retrieval_time,\
#             delta=(first_key_value_average_retrieval_time+1e-6)*2)

def fake_key():
    return f"FAKE KEY {time.time()}"

def fake_value():
    return f"FAKE VALUE {time.time()}"

def average_retrieval_time(table, key):
    time_samples = []
    for _ in range(1000):
        start_time = time.time()
        _ = table[key]
        end_time = time.time()
        time_samples.append(end_time - start_time)
    return sum(time_samples) / float(len(time_samples))

if __name__ == '__main__':
    unittest.main()
