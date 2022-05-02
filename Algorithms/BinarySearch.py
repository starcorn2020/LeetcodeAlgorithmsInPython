# Chr3 Binary Search (Optional)

# Example
# array = [10,11,12,13,14,15]
# index = [0 ,1 ,2 ,3 ,4 ,5 ]

# Step:
# |- initail 2 pointers, start at beginning of array, end at the end of the array.
# |- find the element at the middle of the 2 pointers.
# |_ if element at the middle is bigger than our goal, set end pointer to middle.

def binarySearch(arr,target):
    left = 0
    right = len(arr)-1

    while left<=right:
        mid = (left+right)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

if __name__ == '__main__':

    arr = [1,2,3,4,5,6]
    target = 6

    result = binarySearch(arr,target) #index:

    if result == 1:
        print('Element is not present in the array/')
    else:
        print(f'Element is present at index {result}')