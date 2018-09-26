'''
A number is defined as happy by this process:

Starting with any positive integer, replace the number by the sum of the squares
of its digits, and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers,
while those that do not end in 1 are unhappy numbers.

Hint: if during this process you see the same number twice, the number is not happy.

Sum of squares of a digit:
if number is 123, then the sum of squares is (1 **2) + (2**2) + (3**2)

Example

11 -> 2
2 -> 4
4 -> 16
16 -> 37
37 -> 58
58 -> 89
89 -> 145
145 -> 42
42 -> 20
20 -> 4 ------> repeated, therefore, 11 is not a happy number

7 -> 49
49 -> 97
97-> 130
130 -> 10
10 -> 1 -----> Ends with 1, therefore 7 is a happy number
'''

def isHappy(num):
    visited = set()
    while True:
        if(num == 1):
            print("Happy")
            break
        elif num in visited:
            print("Not happy")
            break
        else:
            visited.add(num)
            num = sumOfSquares(num)


def sumOfSquares(n):
    digits = [int(c) for c in str(n)]
    return sum(digit ** 2 for digit in digits)



