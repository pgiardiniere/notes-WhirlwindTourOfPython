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
l[:3]

l[-3:]  # implicit end of list ... "get last 3 elements"







