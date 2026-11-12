import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    x_np = np.asarray(x, dtype=float)
    y_np = np.asarray(y, dtype=float)
    return float(np.dot(x_np, y_np))
    pass