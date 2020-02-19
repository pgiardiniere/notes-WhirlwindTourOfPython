### Basic Python Operators

# NOTE :: Python 3: Default division is TRUE  division
#                   Second  division is FLOOR division
print(11/2)
print(11//2)
#         Python 2: only division is '/', FLOOR division.
#                   true division for Floating-point ONLY.

# Python 3.5 and up, 'A @ B' denotes matrix product of A and B

### Bitwise Operators
# perform bitwise logical operations on integers

# to get binary representation of nums, use bin()
print( bin(10) )     # output 0b1010, binary 1010
                     # i.e. 1(2^3) + 0(2^2) + 1(2^1) + 0(1^0)
print( bin(4) )      # output 0b100,  binary 100

print( bin(4 | 10) ) # output 1110, binary OR
print( 4 | 10 )      # outputs 14, the base-10 result of binary OR


### Assignment Operations :: behaves exactly like you'd expect
a = 24; print(a)
a += 2      # can sub ANY bitwise or arithemtic op for +

### Comparison Operations ::
# Comparison operators return Boolean "True" or "False"
print ( 25 % 2 == 1 )       # test oddity of num
print ( 66 % 2 == 1 )

# multiple comparisons:
a = 25
print (15 < a < 30)         # outputs 'True'

print ( bin(0)  )   # bitwise inverse of 0 is -1
print ( bin(~0) )   # due to "two's complement int encoding"
print ( bin(-1) )   # scheme python uses for SIGNED ints


### Boolean operations
# Expressed via English long-text,
# i.e. "and", "or", "not"
x = 4
print ( x < 6 and x > 2 )
print ( x > 10 or x % 2 == 0 )
print ( not x < 6 )
# ONLY use the &, |, and ! operators for BITWISE comparison (individual bits) 
# ELSE use 'and', 'or', 'not' to return Boolean vals of entire statements.


print('\n')
### Identity and Membership Operators
a = [1, 2, 3] 
b = [1, 2, 3]
# List of operators:
a is b      # True if   a and b are     identical objects
a is not b  # True if   a and b are not identical objects
a in b      # True if   a is     a member of b
a not in b  # True if   a is not a member of b

print('\n')
# Object Identity is stricter than equality.
print ( a == b )          # True
print ( a is b )          # False, pointers to unique objects
print ( a is not b )      # True
a = [4, 5, 6]
b = a
print ( a is b )          # True

# Membership operators check for membership w/in compound objects
print ( 1 in [1, 2, 3] )        # True
print ( 2 not in [1, 2, 3] )    # False