# Explanation - Container with Most Water - Medium 
# Greedy Algorithm

# Height : [1,8,6,2,5,4,8,3,7]

# Fig
# 
# 8   *         *
# 7   *         *   *
# 6   * *       *   *
# 5   * *   *   *   *
# 4   * *   * * *   *
# 3   * *   * * * * *
# 2   * * * * * * * *
# 1 * * * * * * * * *
#   0 1 2 3 4 5 6 7 8

# Height : [5,3,2,1,4]
# Height : [5,9,2,1,4]


'''
Example:

maxArea(height){
    max_area=0
    n = heights.length
    for(p1=0,p1<n,p1++){
        for(p2=p1+1,p2<n,p2++){
            length = min(height[p1],height[p2])
            width = p2-p1
            area = length * width
            max_area = max(max_area,area)
        }

    }
}

'''


class Solution():

    def searchMaxArea(self,arr) -> int:

        max_area = 0
        n = len(arr)-1
        for i,valuee in enumerate(arr):
            for j in range(i+1,n):
                length = min(arr[i],arr[j])
                width = j-i
                area = length * width
                max_area = max(max_area,area)

        return max_area 

    def test():
        print(123)

if __name__ == '__main__':

    arr = [5,9,2,4]
    s = Solution()
    a = s.searchMaxArea(arr)
    print(a)