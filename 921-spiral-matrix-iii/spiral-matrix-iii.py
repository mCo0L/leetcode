class Solution:
    def spiralMatrixIII(self, m: int, n: int, i: int, j: int) -> List[List[int]]:
        ans=[]
        lb,rb,tb,bb=j,j,i,i
        while(len(ans)<m*n):
            while(j<rb+1):
                if(i<m and j<n and i>=0 and j>=0):ans.append([i,j])
                j+=1
            rb+=1
            while(i<bb+1):
                if(i<m and j<n and i>=0 and j>=0):ans.append([i,j])
                i+=1
            bb+=1
            while(j>lb-1):
                if(i<m and j<n and i>=0 and j>=0):ans.append([i,j])
                j-=1
            lb-=1
            while(i>tb-1):
                if(i<m and j<n and i>=0 and j>=0):ans.append([i,j])
                i-=1
            tb-=1
        return ans