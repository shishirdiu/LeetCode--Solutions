# LeetCode #2: Add Two Numbers

##  Problem Description
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

##  Example
- **Input:** `l1 = [2, 4, 3]`, `l2 = [5, 6, 4]`
- **Output:** `[7, 0, 8]`
- **Explanation:** 342 + 465 = 807. Since the digits are stored in reverse, the result is [7, 0, 8].

##  Approach: Iterative Column Addition
The solution mimics the process of manual addition (the way we add numbers on paper from right to left).

1. **Dummy Head:** Used a `dummy` node to simplify the creation of the result linked list.
2. **Carry Management:** Initialized a variable `carry = 0`. For each step, the sum is calculated as:  
   `Sum = (val1 + val2 + carry)`
3. **Node Creation:** The digit to store in the current node is `Sum % 10`, and the new carry is `Sum // 10`.
4. **Traversal:** Iterated through both lists until both are exhausted and there is no remaining `carry`.

##  Complexity Analysis
- **Time Complexity:** $O(\max(m, n))$  
  Where $m$ and $n$ represent the lengths of `l1` and `l2` respectively. We traverse the lists exactly once.
- **Space Complexity:** $O(\max(m, n))$  
  The length of the new list is at most $\max(m, n) + 1$.

## 🛠️ Data Structure Used
- **Singly Linked List**
- **Language:** Python 3
