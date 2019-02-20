# 868. Binary Gap

  
Given a positive integer`N`, find and return the longest distance between two consecutive 1's in the binary representation of`N`.

If there aren't two consecutive 1's, return0.



* 
**Example 1:**

```
Input: 
22
Output: 
2

Explanation: 

22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.

```

**Example 2:**

```
Input: 
5
Output: 
2
Explanation: 

5 in binary is 0b101.

```

**Example 3:**

```
Input: 
6
Output: 
1
Explanation: 

6 in binary is 0b110.

```

**Example 4:**

```
Input: 
8
Output: 
0
Explanation: 

8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.

```



**Note:**

* `1<= N <= 10^9`

## Solution:

first use bin\(\) that N to binary representation than Record the position of each occurrence of loop 1 and find out their maximum distance

## Code:

```py
class Solution:
    def binaryGap(self, N: 'int') -> 'int':
        blist = list(bin(N).split("b")[1])
        indexList = []
        pre = dist = 0
        for i, c in enumerate(blist):
            if c == "1":
                dist = max(dist, i - pre)
                pre = i
        return dist

```



