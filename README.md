# LeetCode #1: Two Sum

##  Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

##  Example
- **Input:** `nums = [2, 7, 11, 15]`, `target = 9`
- **Output:** `[0, 1]`
- **Explanation:** Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

##  Approach: One-Pass Hash Map
Instead of using nested loops ($O(n^2)$), I used a **Hash Map** (Dictionary in Python) to solve this in linear time.

1. Create an empty dictionary `prevMap` to store the value and its index.
2. Iterate through the array once.
3. For each number `n`, calculate the difference: `diff = target - n`.
4. If `diff` exists in `prevMap`, return the indices `[prevMap[diff], i]`.
5. Otherwise, add the current number and its index to the map.

## Complexity Analysis
- **Time Complexity:** $O(n)$ - We only traverse the list containing $n$ elements once. Each lookup in the table costs only $O(1)$ time.
- **Space Complexity:** $O(n)$ - The extra space required depends on the number of items stored in the hash table, which stores at most $n$ elements.

## 🛠️ Language Used
- Python 3
