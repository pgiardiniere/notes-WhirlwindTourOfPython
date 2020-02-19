### Python variables are pointers
# Assign 4   to   variable x
# dynamically typed pointers, at that.
x = 4
x = "hello"
x = [1,2,3]

# pointers behave like pointers do i.e.
x = [1, 2, 3]
y = x
x.append(4)
print(y)
# will clearly change the value of y, since you're referencing the same list.

# (and doi) we can reassign pointer x without affecting y
x = 14
print(y)

# 'simple types' (analogous to primitives) also behave as you would expect.
x = 15
y = x
x += 5
print("x =", x); print("y =", y)
# however in Python, even simple types are objects.
x = 4.5
print(x.real, "+", x.imag, 'i') # simple types have attributes
print(x.is_integer())           # simple types have methods

# EVERYTHING in Python is an object. object attributes/methods inclusive.
print( type(x.is_integer) )
print( type(x.real) )


L = [1, 2, 3]
L.append(100)
print(L)

