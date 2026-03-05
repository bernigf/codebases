def fib_recursive(n):

    # Time Complexity: O(2^n)
    # Space Complexity: O(n)

    # BASE CASE: Fibonacci of 0 is 0, and Fibonacci of 1 is 1.
    # We stop the recursion here to prevent an infinite loop.
    if n <= 1:
        return n
    
    # RECURSIVE STEP: To find F(n), we must find F(n-1) and F(n-2).
    # This creates a "tree" of function calls.
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):

    # Time Complexity: O(n)
    # Space Complexity: O(1)

    # Handle the starting cases directly.
    if n <= 1:
        return n
    
    # We only need to remember the last two numbers to calculate the next one.
    # a = F(n-2), b = F(n-1)
    a, b = 0, 1
    
    # We loop from 2 up to n.
    for _ in range(2, n + 1):
        # Calculate the next number: current = previous + one before previous.
        # Then we shift: 'a' becomes the old 'b', and 'b' becomes the 'current' sum.
        a, b = b, a + b
        
    return b

# Example usage:
print(fib_recursive(10)) # Output: 55
print(fib_iterative(10)) # Output: 55

