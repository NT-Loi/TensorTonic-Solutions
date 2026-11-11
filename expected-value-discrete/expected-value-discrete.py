import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    xp = []
    for i in range(len(x)):
        xp.append(float(x[i] * p[i]))
    exp_val = sum(xp)
    return exp_val
    pass