# example_usage.py
from gregoryleibniz import gregory_leibniz

# Calculate pi with different numbers of terms
result1 = gregory_leibniz(10**5)
result2 = gregory_leibniz(10**6)
result3 = gregory_leibniz(10**7)

print(f"Using 10^5 terms: π ≈ {result1}")
print(f"Using 10^6 terms: π ≈ {result2}")
print(f"Using 10^7 terms: π ≈ {result3}")
