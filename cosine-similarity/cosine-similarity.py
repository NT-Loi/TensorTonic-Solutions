import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a_np = np.asarray(a, dtype=float)
    b_np = np.asarray(b, dtype=float)
    
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    
    if norm_a == 0.0:
        return 0.0
    if norm_b == 0.0:
        return 0.0

    return float(np.dot(a_np, b_np) / (norm_a * norm_b))
    pass