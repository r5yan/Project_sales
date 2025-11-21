import numpy as np

def generate_random_sales(min_val, max_val, size):
    """
    Generate random sales data between min_val and max_val with
     size numbers of values 
    
    Returns an Array of random integers
    the +1 in max_val is because the start but excludes the end

    """
    return np.random.randint(min_val, max_val + 1, size)