### Covering ::
# General   functions using "def"
# Anonymous functions using "lambda"

#########################
### Functions
#########################
print()                 # just a func
print(2)                # func w/         args
print(1, 2, sep='--')   # func w/ keyword args
# when using keyword args, they must come at end of call

def fibonacci(n):       # no strong-typing params or return
    l = []
    a, b = 0, 1
    while len(l) < n:
        a, b = b, a+b
        l.append(a)
    return l

L = fibonacci(10)
print( L )


def real_imag_conj(val):    # multiple returns go in Tuples
    return val.real, val.imag, val.conjugate()

r, i, c = real_imag_conj(3 + 4j)    # val should be numerical
print(r, i, c)

r, i, c = real_imag_conj(2)
print(r, i, c)

r = real_imag_conj(44)      # type-inference :: r is a tuple
print(r[0])

#########################
### Default arg vals
#########################
def fib(n, a=0, b=1):       # CAN overwrite prior func (don't)
    l = []
    while len(l) < n:
        a,b = b, a+b
        l.append(a)
    return l

f = fib(10);            print( f )  # same as fibonacci()
f2 = fib(10, 0, 2);     print( f2 ) # ordered defaults
f3 = fib(10, b=2, a=0); print( f3 ) # keyword defaults



#########################
### Flexible arguments w/ *args, **kwargs   (expansions)
#########################
# specifying  *    means    "expand this as a sequence"
# specifying  **   means    "expand this as a dictionary"
# 'args', 'kwargs' are just conventional names for these vars

def catch_all(*args, **kwargs):
    print("args   =", args)
    print("kwargs =", kwargs)

catch_all(1, 2, 3, a=3, b=22)
catch_all('a', keyword = 2)

# we can use expansions in function calls too
inputs = 1, 2, 3
keywords = { 'keyword':2 , 'a':3 }
catch_all(*inputs, **keywords)    # similar to prior calls


#########################
### Lambda Functions (anonymous funcs)
#########################
# Everything in Python is an object, including functions 
add = lambda x, y : x + y
print ( add(1, 2) )

# performing definition in this way makes it obvious that we
# can then pass this function as an argument to other funcs.

# ---------------- Begin Example -------------------
# sorted() function returns a sorted list
sorted([2,4,3,1,6,5])

# consider: how to sort a list of dictionaries?
data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
        {'first':'Grace', 'last':'Hopper',     'YOB':1906},
        {'first':'Alan',  'last':'Turing',     'YOB':1912}]

# answer:   specify a sort field using a lambda function
sorted(data, key=lambda item: item['first'])

# ---------------- End Example ---------------------