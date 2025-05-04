Gregory-Leibniz Series for π Calculation
This project explores various implementations of the Gregory-Leibniz series to approximate the mathematical constant π. We examine different programming approaches and their performance characteristics when calculating π through this infinite series.

Mathematical Background
Derivation of the Gregory-Leibniz Series
The Gregory-Leibniz series can be derived through a sequence of calculus operations:

We start with the Taylor series expansion of the function:

$$\frac{1}{1-y} = 1 + y + y^2 + y^3 + \ldots$$

Substituting $y = -x^2$:

$$\frac{1}{1+x^2} = 1 - x^2 + x^4 - x^6 + \ldots$$

The derivative of arctangent is:

$$\frac{d}{dx}(\arctan x) = \frac{1}{1+x^2}$$

Integrating both sides:

$$\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \ldots$$

Using the fact that $\arctan(1) = \frac{\pi}{4}$:

$$\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \ldots$$

Therefore:

$$\pi = 4 \left(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \ldots\right) = 4 \sum_{k=0}^{\infty} \frac{(-1)^k}{2k+1}$$

This is the Gregory-Leibniz series for π.

Implementation Approaches
This project implements the Gregory-Leibniz series using three different approaches:

1. Standard While Loop
The basic implementation uses a while loop to calculate the series term by term:
```
def current_implementation(n):
    x = 1
    i = 1
    while i <= n:
        x += (-1)**i * (1/(2*i+1))
        i += 1
    return 4*x
```
2. Optimized For Loop
An improved implementation using a for loop and avoiding repeated calculations:
```
def improved_implementation(n):
    sum_value = 0
    sign = 1
    
    for i in range(n):
        denominator = 2*i + 1
        sum_value += sign * (1/denominator)
        sign *= -1
        
    return 4 * sum_value
```

3. NumPy Vectorization
A highly optimized implementation using NumPy's vectorized operations:
```
def numpy_implementation(n):
    import numpy as np
    
    # Create array of odd numbers from 1 to 2n-1
    denominators = np.arange(1, 2*n, 2)
    
    # Create array of alternating signs: 1, -1, 1, -1, ...
    signs = np.ones(n)
    signs[1::2] = -1
    
    # Calculate sum
    return 4 * np.sum(signs / denominators)
```
Performance Comparison
The implementations show significant performance differences:

Standard While Loop: Slowest due to Python's interpretation overhead and expensive power operations
Optimized For Loop: Faster by avoiding expensive operations and using more efficient loop structures
NumPy Vectorization: Dramatically faster by leveraging C-compiled operations and avoiding Python's loop overhead
Convergence and Limitations
The Gregory-Leibniz series converges extremely slowly. Even with millions of terms, it provides only a few accurate decimal places of π:


10^6 terms: ~5 correct decimal places
10^7 terms: ~6 correct decimal places
10^8 terms: ~7 correct decimal places
10^9 terms: ~12 correct decimal places

The NumPy implementation faces memory constraints with very large n values (e.g., 10^10) as it needs to allocate large arrays. it requires 75 Gb of ram for 10^10 itterations.

## How to compile the code
- Step 1: Create a Python file
Create a new file named gregory_leibniz.py with the content uploaded in this git.
- Step 2: Using the module in other scripts
Now you can import and use this function in any other Python script, for example you can create a py file named exampleusage.py and copy its content from the one uploaded in this git.
- Step 3: Running the code
You can run the module directly:
```
python gregory_leibniz.py
```
Or import it in another script as shown above and run that script:
```
python example_usage.py
```
