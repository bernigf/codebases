"""

Programming exercise

1) Given string 's'
2) Given an array of string 'words'
3) Rturn the number of words i that are subsequence of s

For example:
- s = "abcde"
- words = ["a","bb","acd","ace"]
- thise would give a output score of 3 as "a", "acd" and "ace" are subsequences of s
- bb is not a subsequence of s as it has 2 'b' chars and there is only one

"""

def is_subsequence(s: str, word: str) -> bool:
    i = 0  # pointer for s
    j = 0  # pointer for word
    
    # Traverse both strings
    while i < len(s) and j < len(word):
        if s[i] == word[j]:   # If characters match
            j += 1            # Move pointer in word
        i += 1                # Always move pointer in s
    
    # If we matched all characters in word → subsequence
    return j == len(word)


def num_matching_subseq(s: str, words: list[str]) -> int:
    count = 0  # number of valid subsequences
    
    for word in words:
        if is_subsequence(s, word):  # Check each word
            count += 1
    
    return count
      
# Example 1
s = "abcde"
words = ["a","bb","acd","ace"]

# Example 2
s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

print(num_matching_subseq(s, words))