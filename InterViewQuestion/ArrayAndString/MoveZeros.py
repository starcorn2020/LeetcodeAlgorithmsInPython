# Explanation - Move Zeroes Brute force Intuition - Easy

# Input : [0,1,0,3,12]
# Output : [1,3,12,0,0]

'''
# Example

moveZeroes(input){
    output = []
    n = input.length
    Loop as i in range(0,n){
        if(input[i] is non-zero){
            output.add(input[i])
        }
    }
    m = output.length
    Loop in range(m,n){
        output.add(0)
    }
}

'''

'''
# Solution by teacher

Class Solution:

    def moveZeros(self, nums: List[int]):
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1 
        
        for x in range(j,len(nums)):
            nums[x] = 0
'''

# My Solution 
def moveZeros(inputArr):

    outputArr = [i for i in inputArr if i != 0]

    for i in range(len(outputArr),len(inputArr)):
        outputArr.append(0)

    return outputArr

if __name__ == '__main__':

    arr = [0,1,0,3,12]
    sortedArr = moveZeros(arr)
    print(sortedArr)