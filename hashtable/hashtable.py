import sys
sys.path.append('../hashtable/linked_list')
from linked_list import LinkedList

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

# we have our hashing function that takes in a string & turns it into a number 
# we have a function that takes that number & make sure it fits in our array, finds index spot (hash_index) aka SLOT
# that number is the index in the array we store value in (put) or look up

#Put: 
# Find the slot for the key 
# Search the linked list for the key
# if Found, update it
# if not Found, make a new hash table entry and add it to the list 

# Get:
# Find the slot for the key 
# Searched the linked list for the key 
# if Found return the value 
# if not found, Return None

# Delete:
# Find the slot for the key 
# Search the linked list for the key 
# If found then delete it from the linked list, then return the deleted node 
# If not found then return none

# Q's to Study:
# What is a hash table load factor?
# how do you resize a hash table? why?
# How hash tables work in general? 
# What are we trying to solve with hash tables?
# How to use a cache with hash?

# A's 
# What are hash tables good at? They search fast, insert & delete fast. 
# Improving run time complexity 

# What are the sorts of things we can search for? When do we want to search for them quickly?
# Anything that can be hashed, we can use it to store & retireve the results of slow operations 
# not just searches but also functions that take long computation, you can use it as a cache 

# Think To Fix: Where am I doing a lot of calcualtion here, where I can save that calculation for future reference?

# Cache Implementation: Create Cache -> cache = {} , 
# Check if Cache is empty -> if n not in cache: cache[n] = fib(n-1) + fib(n-2)
# After check the cache, we have the values in our cache so we can just -> return cache 



class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        # Your code here
        # self.capacity = [None] * MIN_CAPACITY (Old)
        # Goal with linked list is we want to take our hash table that only 
        # has so many slots in it & isntead of storing hash table entries directly in the slots, we're going to 
        # store refrences to the hash table entries that have next pointers that point to the next entrty 
        # we will have a linked list of hash table entries, this will save us when we have collisions 
        self.storage = [LinkedList()] * MIN_CAPACITY
        self.count = 0
        self.capacity = capacity

    def my_hashing_function(self, s): # refactor this, its okay but not good
        self.s = s
        # Turn input string into bytes using encode
        string_bytes = s.encode()

        # Sum - Add all the bytes as one value
        total = 0

        for b in string_bytes:
            total += b
        return total



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # hash_val = my_hashing_function(self)
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """

        # number of things stored in the hash table / number of slots in the array 
        # anything over 1 is over loading 
        # anything less than 1 is light loading = better
        # when computing the load keep track of the count of items in the hash as you go (increment/decrement count)
        # Hash tables use an array for storage, so the load factor would be the number of occupied slots divided by the length of the array
        # As the load factor of your hash table increases, so does the likelihood of a collision
        # Therefore, you need to monitor the load factor and resize your hash table when the load factor gets too large
        # The load factor can also be too small.
        # If the hash table is too large for the data that it is storing, then memory is being wasted
        # you should also resize when the load factor gets too low
        return self.count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        seed = 0
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        hash = offset_basis + seed
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        #changed self.capacity to len(self.capacity) due to error:
        # unsupported operand type(s) for %: 'int' and 'list' 
        # return self.djb2(key) % len(self.capacity)
        return self.fnv1(key) % len(self.storage)

    # O(1)
    def put(self, key, value):

        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # Get slot number with key
      #  slot = self.hash_index(key) (Old)
        
        # Use key to create entry value 
      #  entry = HashTableEntry(key, value) (old)
        # assign value to slot 
      #  self.capacity[slot] = entry (old)

        slot = self.hash_index(key)
        current = self.storage[slot].head
        while current:
            if current.key == key:
                current.value = value
            current = current.next
            
        entry = HashTableEntry(key, value)
        self.storage[slot].insert_at_head(entry)
        self.count += 1





    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # self.put(key, None) (old)
        self.put(key, None)
        self.count -= 1

    # O(1)
    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # Get slot number with key 
       # slot = self.hash_index(key)   (old)

        #check capacity using [slot]
       # entry = self.capacity[slot]
        
        # if is entry, return (get) value
       # if entry:
       #     return entry.value
       # return None

        slot = self.hash_index(key)
        current = self.storage[slot].head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # we are overloading when the load factor is greater that 0.7
        # Your code here
        if self.get_load_factor() > 0.7:
            # if the hash table is overloaded, resisze the hash table
            old_storage = self.storage
            self.storage = [LinkedList()] * new_capacity
            for item in old_storage:
                current = item.head
                while current:
                    self.put(current.key, current.value)
                    current = current.next
            self.capacity = new_capacity

            # You can see that resizing is an expensive operation, so you don’t want to resize too often. 
            # However, when we average it out, hash tables are constant time (O(1)) even with resizing.



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
