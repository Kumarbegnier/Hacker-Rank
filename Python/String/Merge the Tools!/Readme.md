Consider the following:
• A string, 8, of length n where & Co C1... Cn-1-
• An integer, k, where k is a factor of n.
We can split s into
to create string
substrings where each subtring, t;, consists of a contiguous block of characters in s. Then, use each t such that
• The characters in are a subsequence of the characters in t
• Any repeat occurrence of a character is removed from the string such that each character in ; occurs exactly once. In other
words, if the character at some index j in occurs at a previous index <j in t;, then do not include the character in string
น
Given 8 and k, print lines where each line & denotes string u
Example
s='AAABCADDE'
k = 3
There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u1 = 'A'. The second substring has all distinct characters, so u2 = 'BCA'. The third substring has 2 different characters, so u = 'DE'. Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.
Function Description
Complete the merge_the_tools function in the editor below.
merge_the_tools has the following parameters:
⚫ strings: the string to analyze
⚫int k: the size of substrings to analyze
Prints
Print each subsequence on a new line. There will be of them. No return value is expected.
Input Format
The first line contains a single string, s.
The second line contains an integer, k, the length of each substring.
Constraints
• 1 ≤ n ≤ 104, where n is the length of s
• 1≤ k ≤n
• It is guaranteed that n is a multiple of k.                                                                                                                                     ﻿

Sample Input
STDIN
AABCAAADA
3
Function
s = 'AABCAAADA'
k = 3
Sample Output
AB
CA
32
AD
Explanation
Split & into == 3 equal parts of length = 3. Convert each t; to us by removing any subsequent occurrences of non-
distinct characters in t
= "AAB" → 0 = "AB"
1.to=
2. t1
"CAA" 1 =
"CA"
3.12
= "ADA" → u2 = "AD"
