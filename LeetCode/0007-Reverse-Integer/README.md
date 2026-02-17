# LeetCode #7: Reverse Integer

## Problem Description
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range $[-2^{31}, 2^{31} - 1]$, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

## Example
- **Input:** `x = 123`
- **Output:** `321`

- **Input:** `x = -123`
- **Output:** `-321`

- **Input:** `x = 120`
- **Output:** `21`

## Approach: Mathematical Digit Extraction
The problem can be solved by repeatedly extracting the last digit of the number and building the reversed number.

1. **Handle Sign:** Store whether the number is negative or positive, and work with the absolute value.
2. **Reverse Logic:** 
   - Extract the last digit using `x % 10`.
   - Append it to the `res` variable: `res = res * 10 + digit`.
   - Remove the last digit from `x` using integer division `x //= 10`.
3. **Overflow Check:** Before returning, check if the reversed number exceeds the 32-bit signed integer range $[-2147483648, 2147483647]$.

## Complexity Analysis
- **Time Complexity:** $O(\log(x))$ — The number of digits in $x$ is approximately $\log_{10}(x)$.
- **Space Complexity:** $O(1)$ — Only a few variables are used to store the result and sign.

## Tech Stack
- **Language:** Python 3
- **Topic:** Math, Integer Manipulation
