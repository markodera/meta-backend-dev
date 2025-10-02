def is_perfect(n):
    """
    Check if a number is perfect.
    A perfect number equals the sum of its proper divisors.
    Example: 6 = 1 + 2 + 3 (divisors of 6 excluding 6 itself)
    """
    
    # Handle edge cases
    if n <= 1:
        print(f"{n} is not a valid number for perfect check")
        return False
    
    # List to store divisors (excluding the number itself)
    divisors = []
    
    # Find all divisors of n (from 1 to n-1)
    # Check each number to see if it divides n evenly
    for i in range(1, n):
        if n % i == 0:  # If i divides n evenly, it's a divisor
            divisors.append(i)
    
    # Calculate sum of divisors
    divisor_sum = sum(divisors)
    
    # Check if sum of divisors equals the original number
    if divisor_sum == n:
        print(f"{n} is a perfect number! Divisors: {divisors} sum to {divisor_sum}")
        return True
    else:
        print(f"{n} is not perfect. Divisors: {divisors} sum to {divisor_sum}, not {n}")
        return False

# Test cases
print("Testing perfect numbers:")
print("-" * 40)
is_perfect(6)    # Should be perfect
print()
is_perfect(12)   # Should NOT be perfect  
print()
is_perfect(28)   # Should be perfect
print()
is_perfect(1)    # Edge case

print("Fill in the TODO sections and then test your function!")
print("Remember: 6 is perfect because 1 + 2 + 3 = 6")
