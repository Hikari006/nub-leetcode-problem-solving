class Solution:
    def countHomogenous(self, s: str) -> int:
        ans=0
        mod=10**9+7
        for x,y in groupby(s):
            n=len(list(y))
            ans+=n*(n+1)//2
        return ans%mod
        