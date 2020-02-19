### Simple Types in Python ::
# --- Python Scalar Types ---
# ----------------------------------------------
# Type      Example         Description
# ``````````````````````````````````````````````
# int       x = 1           integers
# float     x = 1.0         floating point nums
# complex   x = 1 + 2j      complex nums
# bool      x = True        True/False
# str       x = 'abc'       String: chars//text
# NoneType  x = None        Null values
#
# ----------------------------------------------

### Integers (ints)
x = 1; print ( type(x) )
# unlike most languages, ints do NOT overflow
# they are variable-precision.
print ( 2 ** 200 )
# Python ints up-cast to floats when divided
print ( 5 / 2 )

# PYTHON 2 ONLY -- difference between 'int' and 'long'


### Floating-Point numbers
# can be defined in decimal notation OR exponential
x = 0.000005
y = 5e-6
print ( x == y )

x = 1400000.00
y = 1.4e6
print ( x == y )

# as expected, cast to float as follows:
float(1)

# as usual, floating point comparison is wonky
print ( 0.1 + 0.2 == 0.3 )    # yields False
# caused by binary > decimal (base-2 > base-10) approximation
print( "0.1 = {0:.17f}".format(0.1) )
print( "0.2 = {0:.17f}".format(0.2) )
print( "0.3 = {0:.17f}".format(0.3) )

# specifically, representing a 1/10 digit num requires infinite digits in base-2
# much like 1/3 requires infinite digits in base-10


### Complex Numbers
print ( complex(1, 2) )     # j used instead of i
c = 3 + 4j          # j is 'keyword' - denotes imag
print ( c.real )
print ( c.imag )
print ( c.conjugate() )     # 3 - 4j
print ( abs(c) )    # 3^2 + (4j)^2  absolute magnitude


### String Type
# String created with EITHER 'single' "double" quotes
message = "foobar"
response = "doi"

# example (useful) string funcs/methods.
print ( len(message) )          # 3
print ( message.upper() )       # make all-caps
print ( message.lower() )       # all-lowercase
print ( message.capitalize() )  # first-cap
print ( message + response )    # string concat (NO auto-spacing)
print ( message[0] )            # char indexing
print ( 5 * response )          # * to mult. concat.


### None Type
print ( type(None) )    # None keyword denotes NoneType

# commonly used like "void" returns in other langs
return_value = print('abc')
print ( return_value )


### Boolean Type
result = (4 < 5)
print ( result )
print ( type(result) )
print(True, False)      # Boolean vals CASE SENSITIVE

# construct using bool()
print ( bool(42) )      # numeric nonzero is True
print ( bool(0) )       # numeric    zero is False
print ( bool(None) )    # NoneType is False
print ( bool("text") )  # norm. string is True
print ( bool("") )      # empty string is False
print ( bool([1,2]) )   # norm. list is True
print ( bool([]) )      # empty list is False