# Explanation - Find First and Last Position of Element in Sorted Array - Medium 

# Description

# index : [00,01,02,03,04,05]
# value : [10,11,13,15,17,18] 
# Target = 13
# Return [-2,-2]
 
# If targer not found 
# Return [-1,-1]


'''
Example1:

SearchRange(input,target){
    first = findFirst(input,target)
    last = findLast(input,targer)
    return[first,last]
}

findFirst(input,target){
    n = input.length
    Loop as i in range(0:n){
        if(input[i] == target)
        retrurn i
    }
    return -1
}

findLast(input,target){
    n = input.length
    Loop as i in range(n-1:0){
        if(input[i] == target)
        retrurn i
    }
    return -1
}

Example2:

# index : [00,01,02,03,04,05]
# value : [10,11,11,11,14,15] 
# Target = 11

left = 0
right = len(nums)-1 #4
while(left <= right):
    mid = (len+right)/2 #2
    if(num[mid] == target):
        if(mid==0 || nums[mid-1] != target):
            return mid
        right = mid - 1
    else if(nums[mid] > target):
        right = mid - 1
    else:
        left = mid + 1


'''

from typing import List

class Solution():

    def SearchRange(self,nums: List[int],target: int) -> List[int]:
        
        first = self.findFirst(nums,target)
        last = self.findLast(nums,target)
        return[first,last]

    def findFirst(self,nums: List[int],target: int) -> int:

        left = 0
        right = len(nums)-1

        while(left<=right):
            mid = (left+right)//2
            if nums[mid]==target:
                if mid-1 >= 0 and nums[mid-1] != target or mid == 0:
                    return mid
                right = mid-1
            elif nums[mid] > target:
                right = mid-1 
            else:
                left = mid+1

        return -1

    def findLast(self,nums: List[int],target: int) -> int:

        left = 0
        right = len(nums)-1

        while(left<=right):

            mid = (left+right)//2
            if nums[mid]==target:
                if mid+1 < len(nums) and nums[mid+1] != target or mid == len(nums)-1:
                    return mid
                left = mid+1
            elif nums[mid] > target:
                right = mid-1 
            else:
                left = mid+1

        return -1


if __name__ == '__main__':

    arr = [1,1,1,2,2,2,3,4,5,8]
    s = Solution()       
    ans = s.SearchRange(arr,1)
    print(ans)



