def is_palindrome(n):
    """
    Check if a number is a palindrome.
    A palindrome number reads the same forwards and backwards.
    Example: 121 is palindrome, 123 is not
    """
    
    # Handle negative numbers
    if n < 0:
        print(f"{n} is negative - not a palindrome")
        return False
    
    # TODO: Convert number to string to work with digits
    # YOUR CODE HERE: convert n to a string
    num_str = str(n)
    
    # TODO: Reverse the string
    # Hint: You can use slicing with [::-1] or build it character by character
    # YOUR CODE HERE: create reversed version of num_str
    reversed_str = num_str[::-1]
    
    # TODO: Compare original and reversed
    # Print result and return True/False
    # YOUR CODE HERE
    if num_str == reversed_str:
        print(f"{n} is a palindrome")
        
        return True
    else:
        print(f"{n} is not the palindrome of({num_str} ≠{reversed_str})")
        return False
    

# Test cases - uncomment when ready!
is_palindrome(121)    # Should be palindrome
is_palindrome(123)    # Should NOT be palindrome
is_palindrome(1331)   # Should be palindrome  
is_palindrome(7)      # Should be palindrome (single digit)
is_palindrome(-121)   # Should NOT be palindrome (negative)

print("Fill in the TODOs and test your palindrome checker!")
print("Hint: 121 backwards is still 121!")