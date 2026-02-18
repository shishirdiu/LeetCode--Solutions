# LeetCode #8: String to Integer (atoi) 

## Problem Description
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer. 

The function must handle:
1. **Leading Whitespace:** Ignore any leading whitespace.
2. **Sign:** Check if the next character is '-' or '+'.
3. **Conversion:** Read in characters until the next non-digit character or the end of the input.
4. **Rounding/Clamping:** If the integer is out of the 32-bit signed integer range $[-2^{31}, 2^{31} - 1]$, clamp it to the boundary values.

## Example
- **Input:** `s = "   -42"`
- **Output:** `-42`
- **Input:** `s = "4193 with words"`
- **Output:** `4193`
- **Input:** `s = "words and 987"`
- **Output:** `0` (Since "words" is not a digit)

## Approach: Systematic Parsing
To solve this problem efficiently without using high-level built-in parsing functions, I followed these steps:

1. **Step 1: Whitespace Removal**  
   Used `strip()` to remove leading and trailing whitespaces.
2. **Step 2: Sign Detection**  
   Checked the first character for a negative (`-`) or positive (`+`) sign and set a `sign` variable.
3. **Step 3: Iterative Conversion**  
   Used a `while` loop to traverse the string. For each digit encountered, updated the result: `res = res * 10 + digit`. Stopped immediately when a non-digit character was found.
4. **Step 4: Boundary Handling (Clamping)**  
   Applied the 32-bit signed integer constraints. If the result was less than $-2,147,483,648$, returned the minimum value. If it exceeded $2,147,483,647$, returned the maximum value.

##Complexity Analysis
- **Time Complexity:** $O(n)$ — The string is traversed once, where $n$ is the length of the string.
- **Space Complexity:** $O(1)$ — Only a constant amount of extra space is used for variables (`res`, `sign`, `i`).

## Tech Stack
- **Language:** Python 3
- **Topic:** String Manipulation, Integer Overflow Handling, Input Validation
