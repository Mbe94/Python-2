import sys
from typing import Text
print(sys.path)

import re
texto = "mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte es 3"
result = re.findall('[0-9]+', texto)
print(result)

import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)