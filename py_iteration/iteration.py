"""
TAYLOR SIN FUNCTION by .badian
"""
import math


def sin_(value: float) -> float:
    """sin function Taylor series"""
    accuracy = 10
    result = 0
    for i in range(accuracy):
        result += ((-1) ** i) * (value ** (2 * i + 1) / math.factorial(2 * i +1))
    return result
