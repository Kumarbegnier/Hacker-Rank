

You are given a function f(x) = X2. You are also given K lists. The th list consists of N; elements.
You have to pick one element from each list so that the value from the equation below is maximized:
S=(f(X1) + f(X2) + ... + f(Xx)) %M
X; denotes the element picked from the th list. Find the maximized value Smar obtained.
% denotes the modulo operator.
Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.
Input Format
The first line contains 2 space separated integers K and M.
The next K lines each contains an integer N,, denoting the number of elements in the th list, followed by N; space separated integers denoting the elements in the list.
Constraints
1≤K≤7
1 ≤ M ≤ 1000
1 < N; ≤7
1< Magnitude of elements in list <109
Output Format
Output a single integer denoting the value Smar
Sample Input
3 1000
254
3789
5 5 7 8 9 10
Sample Output
206
Explanation
Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list gives the maximum $ value equal to (52 +92 +102)% 1000 = 206.
