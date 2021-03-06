import hashlib
import random
import struct
import time
from multiprocessing import Pool, cpu_count

# Calculate total sum of slow_calculate() of all numbers starting from 0
# to 500.
# Calculation time should not take more than a minute.
# Use functional capabilities of multiprocessing module.
# You are not allowed to modify slow_calculate function.


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def mult(func, values):
    """Returns time of parallel execution of func"""
    with Pool(cpu_count() * 25) as pool:
        res = sum(pool.map(func, values))
    return res
