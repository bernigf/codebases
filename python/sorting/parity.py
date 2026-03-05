def sort_parity_simple(nums):

    # Time Complexity: O(n)
    # Space Complexity: O(n)

    # STEP 1: Create a new list containing only EVEN numbers.
    # We use the modulo operator (x % 2 == 0). If the remainder is 0, it's even.
    evens = [x for x in nums if x % 2 == 0]
    
    # STEP 2: Create a second list containing only ODD numbers.
    # If the remainder of x / 2 is NOT 0, the number is odd.
    odds = [x for x in nums if x % 2 != 0]
    
    # STEP 3: Concatenate (join) both lists.
    # Since 'evens' comes first, all even numbers will occupy the starting positions.
    return evens + odds

def sort_parity_efficient(nums):

    # Time Complexity: O(n)
    # Space Complexity: O(1)

    # Initialize two pointers at opposite ends of the array.
    # 'i' starts at the beginning (index 0).
    # 'j' starts at the very last element.
    i, j = 0, len(nums) - 1
    
    # Continue the process until the pointers meet or cross each other.
    while i < j:
        # Check if the element at 'i' is ODD and the element at 'j' is EVEN.
        # (nums[i] % 2) will be 1 for odd, (nums[j] % 2) will be 0 for even.
        # If 1 > 0, it means they are in the WRONG order (Odd before Even).
        if nums[i] % 2 > nums[j] % 2:
            # Swap the elements in-place using Python's tuple unpacking.
            # This puts the even number at the front and the odd at the back.
            nums[i], nums[j] = nums[j], nums[i]
            
        # If the number at 'i' is already EVEN, it is in the correct section.
        # We move the pointer forward to check the next element.
        if nums[i] % 2 == 0: 
            i += 1
            
        # If the number at 'j' is already ODD, it is in the correct section.
        # We move the pointer backward to check the previous element.
        if nums[j] % 2 != 0: 
            j -= 1
        
    # Return the modified original list.
    return nums