import math
# Memoization, top-down dynamic programming
# Create the cache to be an empty dictionary to store values. Standard python dictionary  
cache = {}



# this is a quick way to use a hashtable to improve a O(n^2) function (previous function had no cache)
# This function is now O(n)

# You can Memoize functions that take multiple arguments
def fib(n):
    # Base Case 
    if n <= 1:
        return n

    # Check the Cache 
    if n not in cache: # if n is not a key in the cache, then lets add it below, do all the computation 
        # Store Values in the cache 
        cache[n] = fib(n-1) + fib(n-2)  # By taking out the redundent calculation

        # We have values in our cache so just return cache[n] 
        return cache[n]
        
    for i in range(95):
        print(f'{i:3} {fib(i)}')  


def expensive_function(x, y):
    
    # Make a key tuple of the arguments
    # We can use both things as keys to the cache 
    # Python allows all immutable to be key which tuple is 

    key = (x, y)
    if key not in cache:
        cache[key] = expensive_function(n-1) + expensive_function(n-2) # Example only
    return cache[key]



# Inverse Square Root 
# inv_sqrt(x) = 1 / sqrt(x)

# Building the look up table ahead of time 

inv_sqrt = {}

def build_lookup_table():

    for i in range(1, 1000):
        inv_sqrt[i] = 1 / math.sqrt(i)

build_lookup_table()

print(inv_sqrt[3])


# Lets sort a dictionary/ hash table

