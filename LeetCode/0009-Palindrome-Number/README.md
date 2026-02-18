# LeetCode #9: Palindrome Number

## Problem Description
Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

An integer is a palindrome when it reads the same forward as backward. For example, `121` is a palindrome while `123` is not.

## Example
- **Input:** `x = 121`
- **Output:** `true`
- **Input:** `x = -121`
- **Output:** `false` (Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.)
- **Input:** `x = 10`
- **Output:** `false`

## Approach: Mathematical Digit Reversal
While this problem can be solved by converting the integer to a string, I implemented a **mathematical approach** to optimize space complexity and demonstrate core algorithmic logic.

### Steps:
1. **Handle Negative Numbers:** Any negative number is immediately not a palindrome due to the minus sign.
2. **Reverse the Integer:** 
   - Extract digits one by one using the modulo operator (`x % 10`).
   - Build the reversed number: `reversed_num = (reversed_num * 10) + digit`.
   - Remove the last digit from the original number using integer division (`x //= 10`).
3. **Comparison:** After reversing, compare the original number with the reversed result. If they are identical, the number is a palindrome.

## Complexity Analysis
- **Time Complexity:** $O(\log_{10}(n))$ — We divide the input by 10 in every iteration, where $n$ is the input number.
- **Space Complexity:** $O(1)$ — Only a constant amount of extra space is used for variables (No strings or arrays used).

## Tech Stack
- **Language:** Python 3
- **Topic:** Math, Logical Reasoning
