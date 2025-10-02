def countdown_recursive(n):
    """
    Countdown from n to 1 using recursion (function calls itself!)
    
    Think of it like this:
    countdown(3) prints 3, then calls countdown(2)
    countdown(2) prints 2, then calls countdown(1) 
    countdown(1) prints 1, then stops!
    """
    
    # TODO: Base case (when to STOP calling ourselves)
    # This is SUPER IMPORTANT - without this, infinite loop!
    # YOUR CODE HERE: when should we stop?
    if n <= 0:
        print("🚀 Blast off!")
        return  # STOP HERE - no more recursive calls!
    
    # TODO: Do something with current number
    # YOUR CODE HERE: what should we print?
    print()
    
    # TODO: Recursive call (the magic happens here!)
    # Call ourselves with a smaller number
    # YOUR CODE HERE: call countdown_recursive with what number?
    countdown_recursive()

def countdown_loop(n):
    """
    Same thing but with a regular loop (for comparison)
    """
    for i in range(n, 0, -1):
        print(i)
    print("🚀 Blast off!")

# Test both versions
print("=== Recursive Version ===")
# countdown_recursive(5)  # Uncomment when ready!

print("\n=== Loop Version (for comparison) ===") 
countdown_loop(5)

print("\nFill in the recursive version and see the magic!")
print("Remember: recursion = function calling itself with SMALLER input")