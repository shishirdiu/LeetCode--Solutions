# LeetCode #3: Longest Substring Without Repeating Characters

##  Problem Description
Given a string `s`, find the length of the **longest substring** without repeating characters.

##  Example
- **Input:** `s = "abcabcbb"`
- **Output:** `3`
- **Explanation:** The answer is "abc", with the length of 3.

- **Input:** `s = "bbbbb"`
- **Output:** `1`
- **Explanation:** The answer is "b", with the length of 1.

##  Approach: Sliding Window with Hash Map
To solve this in $O(n)$ time, I used the **Sliding Window** technique combined with a **Hash Map** (Dictionary).

1. **Two Pointers:** I used a `left` pointer to mark the start of the window and a `right` pointer (from the loop) to mark the end.
2. **Hash Map:** A dictionary `char_map` stores the **last seen index** of each character.
3. **Updating Window:** 
   - If the current character is already in the map and its index is within the current window (`index >= left`), I move the `left` pointer to `index + 1`.
   - This effectively "slides" the window past the repeated character.
4. **Result:** In each step, I calculate the window size (`right - left + 1`) and update the `max_length`.

## Complexity Analysis
- **Time Complexity:** $O(n)$ — We traverse the string only once with the `right` pointer.
- **Space Complexity:** $O(min(m, n))$ — The size of the Hash Map is bounded by the size of the string ($n$) and the size of the character set ($m$).

## 🛠️ Tech Stack
- **Language:** Python 3
- **Algorithm:** Sliding Window, Hash Map
