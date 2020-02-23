### Generator Expressions vs List Comprehensions:
[n ** 2 for n in range(12)]    # list comp : square bracket
(n ** 2 for n in range(12))    # gen. expr : parens

g = (n ** 2 for n in range(12))
l = list(g)
print ( g )              # Generator object
print ( l, '\n' )              # List created from generator

# Can iterate over a Generator the same as a List ONE TIME (despite no contents)
# g = (n ** 2 for n in range(12))
# for val in l : print(val)
# for val in g : print(val)
# print('\n')

g = (n ** 2 for n in range(12))
print(*l)
print(*g)
print('\n')

#########################
### Infinite Generators :: itertools - count()
#########################
from itertools import count     # recall :: count() use
for i in count():
    print(i, end=' ')
    if i >= 10 : break

# If want a generator to go on forever, just link it to count()
factors = [2, 3, 5, 7]
g = (i for i in count() if all(i % n > 0 for n in factors))
for val in g:
    print(val, end=' ')
    if val > 40 :
        print("\n")
        break

#########################
### Generator Expressions are Single Use (!!!)
#########################
l = [n ** 2 for n in range(12)]
print(*l)
print(*l)

g = (n ** 2 for n in range(12))
print(list(g))
print(list(g))

# Why is it this way? --- Iteration can be stopped and started
g = (n ** 2 for n in range(12))
for n in g:
    print(n, end=' ')
    if n > 30: break
print('\ndo something in between iters')
for n in g:
    print(n, end=' ')   # could be useful for reading in stuff from disk
print('\n')

#########################
### Generator Functions: Using 'yield'
#########################
l1 = [n ** 2 for n in range(12)]
l2 = []
for n in range(12): 
    l2.append(n ** 2)

print(l1)
print(l2)

g1 = (n ** 2 for n in range(12))
def gen():
    for n in range(12): 
        yield n**2
g2 = gen()

print(*g1)
print(*g2)

# Why does this work?
# Generator Functions are just functions using 'yield' keyword, not 'return'
# 'yield' yields a sequence of values

# USE :: to get a fresh generator, we can call the function again
# EX  :: could refactor this code to use a generator func instead of manual redec. of squares

#########################
### Example : prime number generator
#########################
print('\n\n')
l = [n for n in range(2, 40)] # make list, 2 to 39

# remove multiples of 1st value
l = [n for n in l if n==l[0] or n % l[0] > 0]; print(l)
# remove multiples of 2nd value
l = [n for n in l if n==l[1] or n % l[1] > 0]; print(l,'\n')

# we can codify this in a Generator Function
def gen_primes(n):
    """Generate primes up to N"""
    primes = set()
    for n in range(2, n):
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n

print(*gen_primes(40))

print('\n')