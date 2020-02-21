### Built-In Data Structures
# Includes :: Lists, Tuples, Dicts, Sets

# list  [1, 2, 3]           ordered collection
# tuple (1, 2, 3)           Immutable ordered coll
# dict  { 'a':1, 'b':2 }    Unordered (key,val) mapping
# set   {1, 2, 3}           Unordered coll, unique vals

#########################
### Lists
#########################
# Ordered and Mutable, the in-brief notation to declare is
L = [2, 3, 5, 7]
print ( len(L) )    # len(list) returns length of the list

L.append(11)
print ( L )

# Add to concatenate lists
L + [13, 17, 19]
print ( L )

# In-place sort w/ sort()
L = [2, 4, 5, 1, 6, 3]
L.sort()

# NO single-type requirement.
L = [ 1, "two", 3.14, [0,1] ]   # is a valid list


## List Indexing // slicing
L = [2, 3, 5, 7, 11]
L[0]
# negative numbers access `i`th el AWAY from end of list
L[-1]       
L[-2]

# Slices - [Inclusive : Exclusive]
L[0:3]
L[ :3]  # implicit 0   L[:3]
L[:3]

L[-3:]  # implicit end of list ... "get last 3 elements"

L[::2]  # implicit L[0:len(L):2]    "every 2nd el of L" 

L[::-1] # iterate backwards through array (i.e. reverse)

# can assign with slices!
L[0]   = 100        # [100,  3,  5, 7, 11]
L[1:3] = [55, 66]   # [100, 55, 56, 7, 11]

#########################
### Tuples
#########################
t = (1, 2, 3)       # dec w/  parens
t =  1, 2, 3        # dec w/o parens
print(t)

len(t)              # len = 3
t[0]                # direct access

# t[1] = 4          # IMMUTABLE --- throws typeError
# t.append(4)

# tuples often used in Python, see below
x = 0.125
print ( x.as_integer_ratio() )  # (1, 8)

num, denom = x.as_integer_ratio()
print ( num / denom )

#########################
### Dictionaries
#########################
# quite flexible mappings of key-value pairs
numbers = { 'one':1, 'two':2, 'three':3 }

# Item access :: by KEY
numbers['two']      # returns 2

# add stuff in:
numbers['ninety'] = 90

# dictionaries are hashtables, so iterators will NOT 
# print elements in the order in which they were inserted

#########################
### Sets
#########################
# unordered collections of unique items
primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}

## Set methods
# Union         :: elements in either set
primes | odds               # operator syntax 
primes.union(odds)          # method   syntax

# Intersection  :: elements in both sets
primes & odds               # operator syntax
primes.intersection(odds)   # method   syntax

# Difference    :: elements in primes and not in odds
primes - odds               # operator
primes.difference(odds)     # method

# Symmetric Difference :: elements in only 1 set (XOR)
primes ^ odds
primes.symmetric_difference(odds)

#########################
### Niche Data Structures
#########################
# collections.namedtuple    each value in tuple is named
# collections.defaultdict   unspecified keys default to X
# collections.OrderedDict   Dict with Ordered keys


