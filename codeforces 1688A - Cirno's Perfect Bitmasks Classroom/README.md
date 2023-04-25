Cirno's perfect bitmasks classroom has just started!

Cirno gave her students a positive integer x
. As an assignment, her students need to find the minimum positive integer y
, which satisfies the following two conditions:

* x and y>0
* x xor y>0
Where and
 is the bitwise AND operation, and xor
 is the bitwise XOR operation.

Among the students was Mystia, who was truly baffled by all these new operators. Please help her!

Input
The first line of input contains a single integer t
 (1≤t≤103
) — the number of input test cases.

For each test case, the only line of input contains one integer x
 (1≤x≤230
).

Output
For each test case, print a single integer — the minimum number of y
.

Example
inputCopy
7
1
2
5
9
16
114514
1000000
outputCopy
3
3
1
1
17
2
64
Note
Test case 1:

1and3=1>0
, 1xor3=2>0
.

Test case 2:

2and3=2>0
, 2xor3=1>0
