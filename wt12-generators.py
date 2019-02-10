### Attribution of code:
### A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1.
# All comments my own


# from itertools import count
# for i in count():
#     print(i, end=' ')
#     if i >= 10: break

### a basic Erosthenes Sieve implementation using a generator
# print('\nfactor divisible gen print until over 40:')
# factors = [2, 3, 5, 7]
# G = (i for i in count() if all(i % n > 0 for n in factors))
# for val in G:
#     print(val, end=' ')
#     if val > 40: break

#############################################
### List comprehensions can be used multiple times...
# L = [n ** 2 for n in range(12)]
# for val in L:
#     print(val, end=' ')
# print()

# for val in L:
#     print(val, end=' ')

### ... while Generators expire after 1 use
# G = (n ** 2 for n in range(12))
# print(list(G))
# print(list(G))
#############################################

#############################################
### Generator execution can be stopped then restarted from same point
# G = (n**2 for n in range(12))
# for n in G:
#     print(n, end=' ')
#     if n > 30: break

# print("\ndoing something else here...")

# for n in G:
#     print(n, end=' ')
#############################################

#############################################
### With 'yield', we can make generator functions
### another layer of abstraction, which assists in repeated use of complex generators
# L1 = [n ** 2 for n in range(12)]
# L2 = []
# for n in range(12):
#     L2.append(n ** 2)
# print(L1)
# print(L2)

# G1 = (n ** 2 for n in range(12))
# def gen():
#     for n in range(12):
#         yield n**2
# G2 = gen()
# print(*G1)
# print(*G2)

#############################################
### Yield+Gen use-case: prime number generator (revisited)
### First, the less-elegant, more explicit, List Comprehension method:

# Generate list of candidates
L = [n for n in range(2, 40)]
print(L)
# Remove all multiples of the first value in L (i.e. 2)
L = [n for n in L if n == L[0] or n %L[0] > 0]
print(L)
# remove all multiples of the second value
L = [n for n in L if n == L[1] or n % L[1] > 0]
print(L)
# remove all multiples of the third value
L = [n for n in L if n == L[2] or n % L[2] > 0]
print(L)
print()
### Now, we encapsulate this logic in a generator function:

## I don't understand precisely how the 2 from n[0] is applied to p in primes for the initial case
## but after that, it is simply iterating each number from 2 to an arbitrary N
## if ANY number added to primes CANNOT cleanly divide with remainder 0, add current number to primes, return & continue (i.e. 'yield')
def gen_primes(N):
    """Generate primes up to N"""
    primes = set()
    for n in range(2, N):
        if all (n % p > 0 for p in primes):
            primes.add(n)
            yield n

print(*gen_primes(100))