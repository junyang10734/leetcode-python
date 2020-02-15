1. Two Sum
* array / hash table (easy)
* 注意使用 hash map 可以大大加快速度， 尽量避免循环嵌套  
<br />

2. Add Two Numbers
* linked list / math (medium)
* 先求和，再构建链表，暴力解法，但效率可接受
* list[::-1] 将数组倒序  
<br />

3. Longest Substring Without Repeating Characters
* hash table / two points / string / sliding window (medium)
* two points: 维护左右两个指针，将子字符串中元素存入set，发现重复元素，则维护指针和set
* hash table: 左右两个指针，将包含在内的子字符串内元素及其坐标存入hash table，右指针向右遍历，若hash table中存在右指针所有元素，则更改左指针  
<br />

5. Longest Palindromic Substring
* string / DP
* 维护一个二维数组dp， 若s[i]到s[j]是回文字符串，则dp[i][j]为1， 否则为0
* i,j相同时，dp[i][i] = 1
* i-j==1时，若s[i]==s[j]，则dp[i][j] = 1
* i-j>1时，若 dp[i+1][j-1]==1 && s[i]==s[j]，则dp[i][j] = 1
* 注意，因为dp[i][j]可能要根据dp[i+1][j-1]计算得出，所以应留意循环条件，将j作为外层循环，内部嵌套i的循环