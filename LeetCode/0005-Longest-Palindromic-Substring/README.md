# LeetCode #5: Longest Palindromic Substring 

## Problem Description
Given a string `s`, return the **longest palindromic substring** in `s`. 
A string is a palindrome if it reads the same forward as backward.

##  Example
- **Input:** `s = "babad"`
- **Output:** `"bab"` (Note: "aba" is also a valid answer)

- **Input:** `s = "cbbd"`
- **Output:** `"bb"`

##  Approach: Expand Around Center
A palindrome mirrors around its center. The core idea is that there are $2n - 1$ possible centers for a palindrome in a string of length $n$. 

### Logic:
1. **Iterative Centering:** We iterate through each character in the string, treating it as a potential center of a palindrome.
2. **Two Scenarios:** 
   - **Odd Length:** A palindrome where the center is a single character (e.g., "aba", center is 'b').
   - **Even Length:** A palindrome where the center is between two characters (e.g., "abba", center is 'bb').
3. **Expansion:** For each center, we expand outwards as long as the characters match and we remain within the string boundaries.
4. **Update Max:** Whenever we find a longer palindrome, we store it as our current result.

##  Complexity Analysis
- **Time Complexity:** $O(n^2)$  
  We iterate through the string of length $n$, and for each character, we expand outwards (which takes at most $O(n)$).
- **Space Complexity:** $O(1)$  
  Unlike the Dynamic Programming approach which requires $O(n^2)$ space, this method only uses a few pointers to keep track of indices, making it highly memory efficient.

## Tech Stack
- **Language:** Python 3
- **Algorithm:** Two-Pointers, String Expansion
