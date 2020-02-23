### Explicit module import
import math
print(math.cos(math.pi))

### explicit module import by alias
import numpy as np
print(np.cos(np.pi))

### explicit import of module contents (to local namespace)
from math import cos, pi
print(cos(pi))

### implicit import of module contents (to local namespace)
### commented below to squelch errors
from math import *  
print(sin(pi) ** 2 + cos(pi) ** 2)

    # the above is not a recommended method of import. Per the 'problems' in VSCode console,
    # there are 50 funcs in math module imported to local namespace, of which only 3 are used
    # if I had functions before this import of the same name, they would be implicitly overwritten
