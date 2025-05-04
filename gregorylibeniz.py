# gregory_leibniz.py
import numpy as np
from math import pi

def gregory_leibniz(n):
    """
    Calculate pi using the Gregory-Leibniz series with n terms.
    
    Args:
        n (int): Number of terms to use in the approximation
        
    Returns:
        float: Approximation of pi
    """
    # Create array of odd numbers from 1 to 2n-1
    denominators = np.arange(1, 2*n, 2)
    
    # Create array of alternating signs: 1, -1, 1, -1, ...
    signs = np.ones(n)
    signs[1::2] = -1
    
    # Calculate sum
    return 4 * np.sum(signs / denominators)

# This part only runs when the script is executed directly, not when imported
if __name__ == "__main__":
    calc = gregory_leibniz(1*10**6)
    print("The Gregory-Leibniz series approximation of pi is:", calc)
    print("Actual value of pi:", pi)
    print(f"Error: {abs(calc-pi)/pi*100:.8f}%")
