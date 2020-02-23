### Recall: 3 types of errors
# Syntax (compile-time), Runtime, Semantic (logic/intent fail)

#########################
### Runtime Errors
#########################
# print(QWOP)     # NameError: name 'QWOP' is not defined
# 1 + 'abc'       # TypeError: unsupported operand type
# 2 / 0           # ZeroDivisionError: division by zero
l = [1, 2, 3]
# l[1000]         # IndexError: list index out of range

#########################
### Error Handling --- "Try: Except:" clauses
#########################
try:
    print("stuff")
except:
    print("that stuff failed")

try:
    print("BREAKIN THE LAW, BREAKIN THE LAW")
    x = 1/0
except:
    print("that was dumb")

def safer_division(a, b):
    try: 
        return a/b
    except ZeroDivisionError:
        return 1E100

print ( safer_division(1, 2) )
print ( safer_division(2, 0) )
#print( safer_division(1, '2'))     # ONLY 0-Division caught

#########################
### Raising Exceptions
#########################
# raise RuntimeError("lol y u do dis. the program is fine")

def fibonacci(n):
    if n < 0: raise ValueError("num must be non-negative")
    l = []
    a, b = 0, 1
    while len(l) < n:
        a, b = b, a+b
        l.append(a)
    return l

print ( fibonacci(10) )
#print( fibonacci(-10))     # throws the declared ValueError

# book makes example of feeding using its own try-catch block

#########################
### More with Exceptions
#########################
# Access the error message by saving the exception to var.
try:
    x = 1/0
except ZeroDivisionError as err:
    print("Error class is:  ", type(err))
    print("Error message is:", err)

# Defining entirely new (custom) exceptions
class customError(ValueError):
    pass

# raise customError("with some descriptive text")

try:
    print("do stuff")
    raise customError("descriptive msg here")
except customError:
    print("y did you raise that tho")

#########################
### Try-Except-Else-Finally
#########################
# Try     ::    Attempt to run this 
# Except  ::    If 'try' fails ---> this runs
# Else    ::    If 'try' Success -> this runs
# Finally ::    Runs in all cases
try:        print("do things")
except:     print("the things  throw an exception")
else:       print("the things !throw an exception")
finally:    print("this always happens - usually for cleanup")

