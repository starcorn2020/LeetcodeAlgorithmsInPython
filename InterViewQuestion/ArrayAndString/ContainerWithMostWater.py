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
    while(l<r){
        length = min(heights[l],heights[r])
        width = r-l
        area = length*width
        maxarea = max(maxarea,area)
        if heights[l]<heights[r]:
            l+=1
        else:
            r-=1
    }
}

'''
from typing import List
class Solution():

    def maxArea(self,height:List[int]) ->int:

        maxarea = 0
        l = 0
        r = len(height)-1

        while(l<r):

            maxarea = max(maxarea,min(height[l],height[r])*(r-l))
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1

        return maxarea

if __name__ == '__main__':

    arr = [5,9,2,4]
    s = Solution()
    a = s.maxArea(arr)
    print(a)

