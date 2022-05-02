# Explanation - Valid Mountain Array - Easy

# Input : [3,5,5]
# Output : false

# Input : [0,3,2,1]
# Output : true


'''
# Example
i = 1

# Go to up
while(i < len(A) and A[i] > A[i-1]):
    i+=1

if (i==1 or i == len(A)):
    return false

# Go to down
while(i < len(A) and A[i] < A[i-1]):
    i+=1

return (i == len(A))

'''

from typing import List
class Solutin:

    def vaildMountain(self, arr:List[int]) -> bool:

        if (len(arr)<3):
            return False

        i = 1
        while(i<len(arr) and arr[i] > arr[i-1]):
            i +=1

        if (i==1 or i == len(arr)):
            return False

        while(i < len(arr) and arr[i] < arr[i-1]):
            i+=1

        return i == len(arr)
        
if __name__ == '__main__':

    arr = [1,2,3,4,5,3,2,1,0]
    s = Solutin()
    a = s.vaildMountain(arr)
    print(a)