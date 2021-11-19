import hashlib
import random
import struct
import time
from multiprocessing import Pool

# Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
# Calculation time should not take more than a minute.
# Use functional capabilities of multiprocessing module.
# You are not allowed to modify slow_calculate function.


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def mult(func):
    """Returns time of parallel execution of func"""
    values = [x for x in range(500)]
    start = time.time()
    with Pool(50) as pool:
        pool.map(func, values)
    end = time.time()
    return end - start
