21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
<!-- **Note:**  -->

**Example 1:**
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**
```
Input: list1 = [], list2 = []
Output: []
```

**Example 3:**
```
Input: list1 = [], list2 = [0]
Output: [0]
```

**Clarification:**
```
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
```

## Solution:

1. 基本檢核去除空值
2. in-place , iteratively

## code:

<!-- - java
  - Code
    ```java
    class Solution {
    }
    ``` -->
- python
    ```py
    class Solution:
        # 解法一
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if None in (list1, list2):
                return list1 or list2
            dummy = cur = ListNode(0)
            dummy.next = list1
            while list1 and list2:
                if list1.val < list2.val:
                    list1 = list1.next
                else:
                    nxt = cur.next
                    cur.next = list2
                    tmp = list2.next
                    list2.next = nxt
                    list2 = tmp
                cur = cur.next
            cur.next = list1 or list2
            return dummy.next
        # 解法二
    ```
