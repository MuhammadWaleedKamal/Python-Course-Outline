# Importing Modules

## What are Modules?

Files containing Python code.

## Import Styles

```python
# Import module
import math

# Import from module
from math import sqrt

# Import with alias
import numpy as np

# Import all
from math import *
```

## Common Modules

### math
```python
import math
math.sqrt(16)        # 4
math.pi              # 3.14159
math.floor(3.7)      # 3
```

### random
```python
import random
random.randint(1, 10)        # Random int 1-10
random.choice([1, 2, 3])     # Pick random
random.shuffle(list)         # Shuffle list
```

### datetime
```python
from datetime import datetime
now = datetime.now()
year = now.year
```

### os
```python
import os
os.getcwd()          # Current directory
os.listdir()         # List files
```

### collections
```python
from collections import Counter
c = Counter([1, 2, 2, 3, 3, 3])
# Counter({3: 3, 2: 2, 1: 1})
```

## Installing Packages

```bash
pip install package-name
pip install requests
pip install numpy
```

## Creating Your Own Module

**mymodule.py**
```python
def greet(name):
    return f"Hello, {name}!"
```

**main.py**
```python
from mymodule import greet
print(greet("Ali"))
```
