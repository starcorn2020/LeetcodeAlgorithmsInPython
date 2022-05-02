# Chr 4 Sliding Window (Optional)

# Example
# N = 4, K = 2
# array = [80,-50,90,100]

# Step:
# |- Start ar index 0, find sum of k elements.
# |_ Move to the next index and find the sum of k elements from it.


'''
Example 

Function maxSum(arr,k):
    max_sum = NEGATIVE_INFINITY
    n = arr.length
    Loop as i in range 0<n-k+1:
        currnet_sum = 0
        Loopt as j in range 0<k:
            currnet_sum += arr[i+j]

        max_sum = max(current_sum,max_sum)
    
    return max_sum

'''

def maxSum(arr,WindowSize):
    arraySize =len(arr)
    # Check input 
    if arraySize <= WindowSize:
        print("Invalid Operation")
        return -1 
    
    # Define the max sum
    window_sum = sum(arr[i] for i in range(WindowSize))
    max_sum = window_sum

    # Sliding Windows to search answer.
    for i in range(arraySize-WindowSize):
        window_sum = window_sum - arr[i] + arr[i+WindowSize]
        max_sum = max(window_sum,max_sum)

    # Return answer
    return max_sum

if __name__ == '__main__':

    arr = [80,-50,90,100]
    k = 2 
    answer = maxSum(arr,k) #answer is 190
    print(answer)