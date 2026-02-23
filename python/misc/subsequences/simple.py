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

def subseqs(s: str, words: list[str]) -> int:
  
  ss_count = 0 # subsequences counter, always start at 0
  
  for w in words:
    
    # Convert full 's' to a new list of chars on every iteration
    tmp_base_list = [char for char in s]
    
    # Convert each word to a list of chars
    tmp_word_list = [char for char in w]
    
    for char in w:
      if char in tmp_base_list:
        tmp_base_list.remove(char)
        tmp_word_list.remove(char)
    
    if len(tmp_word_list) == 0:
      # No chars left -> w it's a subsequence of s
      ss_count += 1
        
    print(f"Processed word {w} -> chars after removal = {tmp_word_list}")

  print(f"\nTotal subsequences in s: {ss_count}\n")

# Example 1
s = "abcde"
words = ["a","bb","acd","ace"]

# Example 2
s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

subseqs(s, words)