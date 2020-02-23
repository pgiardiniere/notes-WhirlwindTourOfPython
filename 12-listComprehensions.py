# List Comprehensions

#########################
### Basic List Comprehensions
#########################
# allow us to circumvent constructing lists with for loops
l = []                       # The Old Way 
for n in range(12):
    l.append(n**2)

[n ** 2 for n in range(12)]  # Comprehension way

# General Syntax:
# [ `expr` for `var` in `iterable` ]

### Multiple iteration --- use tuples!
[(i, j) for i in range(2) for j in range(3)]

### Conditionals on the Iterator
[i for i in range(20) if i % 3 > 0] #S={i|0<=i<20, 3!|i, i∈I}

l = []                  # equivalent old-school construction:
for val in range(20):
    if val % 3: 
        l.append(val)

### Conditionals on the Value
# C code      :: single-line conditional operator ?
# int absval = (val < 0) ? -val : val 

# Python code :: single-line conditional operator if-else
val = -10
val if val >= 0 else -val

# if 3 !| val ->  val in list.
# if  2 | val -> -val. 
[val if val % 2 else -val
 for val in range(20) if val % 3]

#########################
### Other comprehensions
#########################
{   n**2 for n in range(12) }     # Set  comprehension
{ n:n**2 for n in range(12) }     # Dict comprehension

{ a % 3 for a in range(1000) }    # a = {0, 1, 2}

# GENERATOR EXPRESSION ---- see next chapter for deets
( n**2 for n in range(12) )