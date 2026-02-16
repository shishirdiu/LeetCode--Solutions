# LeetCode #4: Median of Two Sorted Arrays (Hard)

##  Problem Description
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the **median** of the two sorted arrays.

##  Example
- **Input:** `nums1 = [1, 3]`, `nums2 = [2]`
- **Output:** `2.00000`
- **Explanation:** Merged array = [1, 2, 3] and the median is 2.

##  Approach: Two-Pointer Merge
Since both arrays are already sorted, I used a **Two-Pointer** technique to merge them into a single sorted array. This is a robust and intuitive approach to finding the median.

1. **Merging:** I used two pointers (`i` and `j`) to compare elements from `nums1` and `nums2` and append the smaller one to a new `merged` list.
2. **Handling Remaining Elements:** After one array is exhausted, the remaining elements from the other array are appended to the `merged` list.
3. **Finding Median:** 
   - If the total number of elements ($n$) is **odd**, the median is the middle element: `merged[n // 2]`.
   - If the total number of elements is **even**, the median is the average of the two middle elements: `(merged[n // 2 - 1] + merged[n // 2]) / 2.0`.

##  Complexity Analysis
- **Time Complexity:** $O(m + n)$ — We traverse through both arrays exactly once.
- **Space Complexity:** $O(m + n)$ — We create a new array to store the merged elements.

##  Tech Stack
- **Language:** Python 3
- **Algorithm:** Two-Pointer, Merge Sort (Partial)
