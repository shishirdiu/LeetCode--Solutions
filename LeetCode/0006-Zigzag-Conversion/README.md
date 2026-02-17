# LeetCode #6: Zigzag Conversion 

##  Problem Description
The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this:
P A H N
A P L S I I G
Y I R
And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows.

##  Example
- **Input:** `s = "PAYPALISHIRING"`, `numRows = 3`
- **Output:** `"PAHNAPLSIIGYIR"`

- **Input:** `s = "PAYPALISHIRING"`, `numRows = 4`
- **Output:** `"PINALSIGYAHRPI"`
  **Explanation:**
  P     I    N
  A   L S  I G
  Y A   H R
  P     I

##  Approach: String Simulation
The most efficient way to solve this is by simulating the zigzag process using an array of strings to represent each row.

1. **Edge Case:** If `numRows` is 1 or the string length is less than `numRows`, the zigzag doesn't change the order. Return the string immediately.
2. **Row Preparation:** Initialize a list of empty strings, where each element corresponds to a row in the zigzag pattern.
3. **Direction Control:**
   - Use an `index` to track the current row.
   - Use a `step` variable (initially 1) to move down the rows. 
   - When we hit the first row (`index == 0`), we set the direction to move down (`step = 1`).
   - When we hit the last row (`index == numRows - 1`), we set the direction to move up (`step = -1`).
4. **Traversal:** Iterate through each character in the string, append it to the current row, and update the `index`.
5. **Final Result:** Join all strings in the row array to produce the final converted string.

##  Complexity Analysis
- **Time Complexity:** $O(n)$  
  We iterate through the entire string once, where $n$ is the length of the string.
- **Space Complexity:** $O(n)$  
  We store the characters in a list of strings, which in total takes $O(n)$ space.

##  Tech Stack
- **Language:** Python 3
- **Algorithm:** Simulation, String Manipulation
