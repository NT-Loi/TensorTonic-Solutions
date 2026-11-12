import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A_np = np.asarray(A, dtype=float)
    return A_np.T
    pass
