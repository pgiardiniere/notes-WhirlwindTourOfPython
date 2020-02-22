# Control flow :: exists

### Conditionals - python tweest
x = -15
if x == 0:
    print(x, "zer")
elif x > 0:
    print(x, "pos")
elif x < 0:
    print(x, "neg")
else:
    print(x, "is WACK yo")


if x == -15: print("ohai")  # Must include colon, even sameline


#########################
### For loops --- zee python tweest. 
#########################
# java-speak > Python: ALL for loops are for-each loops
# object to the right of "in" must be some Python iterator.
for n in [2, 3, 5, 7]:
    print(n, end=' ')
print()

for i in range(10):
    print(i, end=' ')
print()

# range() works like that for obvious reasons - array iters.
# If specifying 2 bounds, remember lower is INC, upper is EXC
print( range(5, 10) )
print( range(0, 10, 2) )        # 3rd param is freq.

# python 3 :: range produces iterable object
# python 2 :: range produces list

#########################
### while loops
#########################
# works like you'd expect
i = 0
while i < 10:
    print(i, end=' ')
    i += 1
print()

# break and continue as expected
for n in range(20):         # print the odd numbers
    if n % 2 == 0:
        continue
    print(n, end=' ')
print()

# use break to print fibonacci nums (up to certain point)
a, b = 0, 1
amax = 100
L = []

while True:
    (a, b) = (b, a+b)
    if (a > amax): break
    L.append(a)
print(L)


#########################
### Loop - Else
#########################
# similar to if-else, loop-else executes iff loop execution
# ends naturally ( i.e. without 'break'ing ) 

L = []
nmax = 30

for n in range(2, nmax):
    for factor in L:
        if n % factor == 0:
            break
    else:               # no break encountered
        L.append(n)
print('\nsieve is', L)

