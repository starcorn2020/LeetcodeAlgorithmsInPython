# Chr2 Big O Notations

#  Fix 2 problems
#  |- 1. Efficiency
#  |- 2. Space

# Example
# Which is better?

# A
nums =  [1,2,3,4]
n = len(nums)
print(f"Sum of array : {n*(n+1)/2}")

# B
nums =  [1,2,3,4]
n = len(nums)
sum=0
for i in range(0,n):
    sum+=nums[i]
print(f"Sum of array : {sum}")

# ANS : A is better than B

# Formalizing Big O
# *Linear f(N) => f(N) = N

# *Quadratic f(N) => f(N) = N^2

def quadratic(n):
    for i in range(0,n):
        for j in range(0,n):
            print('This is quadratic')

# *Constant f(N) => f(N) = 1

# Constant N
def sumUpToN(n):
    return n*n(n+1)/2

# Mutiple N
def sumUpToN(n):
    sum=0
    for i in range(0,n+1):
        sum+=1
    return sum

# Mutiple N 
def printTwice(n):
    for i in range(0,n):
        print(f"First Loop : {i}")

    for i in range(0,n,-1):
        print(f"Second Loop : {i}")

# Big O Simplification

# Igonre Constants
# O(aN+b) = O(N)
# O(5N+3) = O(N)
# O(Constant) = O(1)
# O(500) = O(1)
# 5N^2 = O(N^2)

# Igonre smaller terms
# 5N^2+3N+1 = O(N^2)

# Space Complexity

'''
# example A
Function SumUpTo(arr):
    sum = 0
    n = len(arr)
    Loop as i from(0,n):
        arr.add(i)
    return arr

# example B
Function getArrUpTo(n):
    arr = []
    Loop as i from (0,n):
        arr.add(i)
    return arr

# example B in Space Complexity is better than example A
'''

# Hash Table : O(N)
# Stacks : O(N)
# Queue : O(N)
#         O(N)
# Array : O(N)
# 2d Array : O(MN)

# Logarithms
# Log -> Math mark
