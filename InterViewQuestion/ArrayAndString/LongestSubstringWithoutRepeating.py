


'''
Examle:

lengthOfLongestSubstring(input){

    if(input.length<=1) return input.length
    max_length = 0
    for(L=0,L<input.length,L++){
        seenCharacters{}
        current_length=0
        for(R=L,R<input.length,R++){
            currentChar=input(R)
            if(seenCharacters INCLUDES currentChar){
                break
            }
            current_length+=1
            seenCharacters[currnetChar]=true
            max_length = max(max_length,current_length) #max(3,1)=3
        }
    }
    return max_length
}

'''

class Solutin():


    def findAns(self,s:str) -> int:

        m = {}
        left = 0
        right = 0
        ans = 0
        n = len(s)
        while(left < n and right < n):
            el = s[right]
            if el in m:
                left = max(left,m[el]+1)
            m[el] = right

            ans = max(ans,right-left+1)
            right+=1

        return ans



if __name__ == '__main__':

    strr = 'asoiijuiuhgrfsdyujuihioiioooii6trdasdg'
    s = Solutin()
    ans = s.findAns(strr)
    print(ans)