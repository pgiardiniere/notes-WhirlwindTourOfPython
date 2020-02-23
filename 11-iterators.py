# Iterators, recall in Python 3, range() return iter:
for i in range(10) : print (i, end=' ')
print('\n')

#########################
### Iterating over lists
#########################
for value in [2, 4, 6, 8, 10] : print( value + 1, end=' ')
print('\n')

# works b/c Python interpreter checks your obj has 'iterator' interface
print ( iter([2, 4, 6, 8, 10]) )
print ( iter )     # iter is func, cannot declare iters as it
print ( next )

I = iter([2, 4, 6, 8, 10])
print(next(I))  # 2
print(next(I))  # 4, and so on if keep calling
print('\n')

#########################
### range() iterators & uses
#########################
# Range iterator object != List iterator object.
print ( iter(range(10)) )

n = 10 ** 12
for i in range(n):          # big range is still performant
    if i >= 10 : break
    print(i, end=', ')
print('\n')

from itertools import count  # count() returns infinite iter.
for i in count():
    if i >= 10 : break
    print(i, end=', ')
print('\n')

#########################
### More useful iterators 
#########################
# We have our very first mention of "Pythonic" stuff

# ---------- enumerate() ----------
l = [2, 4, 6, 8, 10]
for i in range(len(l)):     # OLD way of array index tracking
    print(i, l[i])

for i, val in enumerate(l): # enumerate() way  index tracking
    print(i, val)

# ---------- zip() ----------------
# zip is used to iterate over multiple lists simultaneously
left  = [2, 4, 6,  8, 10] 
right = [3, 6, 9, 12, 15]

for lval, rval in zip(left, right):
    print(lval, rval)

# what if lists are different lengths? 
# SHORTER length determines zip return value

# ---------- map() & filter() ----------------
# map() takes function and applies to the vals in an iterator
#       successive transformation (mapping, doi)
square = lambda x : x ** 2
for val in map(square, range(10)):
    print(val, end=' ')
print('\n')

# filter() takes boolean func and applies to the vals in iter
#          successively returns any True vals (filtering, doi)
is_even = lambda x : x % 2 == 0
for val in filter(is_even, range(10)):
    print(val, end=' ')
print('\n')

# both of these funcs (part of Python 'functools' module) 
# are understandably useful for functional programing 

# NOTE: also see pytoolz, it extends "itertools", "functools"
# for data analysis tasks.

#########################
### Iters as function args
#########################
# Recall :: *args.  as a sequence expansion, it also works with iterators

print( *range(10) )     # now THAT'S compact. And it newlines !!! !!! !!!
print( *map(lambda x : x ** 2, range(10)) )     # omg, 1 freaking line

# the * expansion also allows us to UN-zip() function iterators
# ( possible since zip() returns an iterator on Tuples )
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
z = zip(l1, l2)
print(*z)

z = zip(l1, l2)         # re-initialize iterator - exhausted by print expansion
new_tuple1, new_tuple2 = zip(*z)
print(new_tuple1, new_tuple2)


#########################
### Specialized Iterators: itertools
#########################
# itertools, beyond count(), contains many useful iterators.
from itertools import permutations
p = permutations(range(3))
print(*p)                       # (0, 1, 2) (0, 2, 1) (1, 0, 2) ...

from itertools import combinations
c = combinations(range(4), 2)
print('\n',*c)                  # (0, 1) (0, 2) (0, 3) (1, 2) (1, 3) (2, 3)

from itertools import product   # Product iterates over all sets of pairs b/w 2 iterables
p = product('ab', range(3))
print(*p)                       # ('a', 0) ('a', 1) ('a', 2) ('b', 0) ...

# Iterators AREN'T storing lists - permutation() occupies negligible memory
# Frustratingly, there is NO way to output the Length of an iterator
# So the usefulness of these functions is (apparently) limited strictly to enumerating/counting each element

