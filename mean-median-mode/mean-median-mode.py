from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x_np = np.asarray(x, dtype=float)

    mean = float(np.mean(x_np))
    median = float(np.median(x_np))

    from collections import Counter
    counts = Counter(x)
    max_freq = max(counts.values())
    mode = None
    for key in counts.keys():
        if counts[key] == max_freq:
            if mode is not None:
                if mode > key:
                    mode = float(key)
            elif mode is None:
                mode = float(key)

    res = {"mean": mean, 
           "median": median,
           "mode": mode}
    return res
    pass