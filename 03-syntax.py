# single line comments denoted by #.

# if you want multi-line comment, use a multiline string
'''
multi-line strings on their own produce no bytecode
this is why they are acceptable to use as comments

Could also use your IDEs comment shortcut instead.
'''

midpoint = 5

lower = []; upper = []

for i in range(10):
    if (i < midpoint):
        lower.append(i)
    else:
        upper.append(i)
    
print("lower:", lower)  # Python auto-adds spaces.
print("upper: ", upper) # So don't do this.


# Multi-line statement :: Use '\' or Parens.
x = 1 + 2 + 3 + 4 +\
    5 + 6 + 7 + 8

y = (1 + 2 + 3 + 4 +
     5 + 6 + 7 + 8)

print("x =", x, "and y =", y)