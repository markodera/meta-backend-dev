def fizzbuzz_custom(start, end, rules):
    """
    Custom FizzBuzz with user-defined rules!
    
    Args:
        start: Starting number
        end: Ending number  
        rules: Dictionary like {3: "Fizz", 5: "Buzz", 7: "Pop"}
    
    Example: fizzbuzz_custom(1, 20, {3: "Fizz", 5: "Buzz", 7: "Pop"})
    """
    
    for i in range(start, end + 1):
        output = ""
        
        # TODO: Check each rule and build the output string
        # YOUR CODE HERE: Loop through rules and check if i is divisible
        for key, value in rules.items():
            if i % key == 0:
                output += value
        # TODO: If no rules matched, print the number itself
        # YOUR CODE HERE: Handle the case when output is empty
        if output == "":
            output = str(i)
        print(output)  # What should we print?

# Test cases
print("=== Classic FizzBuzz (1-15) ===")
fizzbuzz_custom(1, 15, {3: "Fizz", 5: "Buzz"})

print("\n=== Triple Rules (1-30) ===") 
fizzbuzz_custom(1, 100, {3: "Fizz", 5: "Buzz", 7: "Pop"})

print("\n=== Your Custom Rules ===")
# TODO: Create your own rules!
fizzbuzz_custom(1, 20, {2: "Even", 4: "Quad", 6: "Hex"})