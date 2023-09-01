class Solution:
    def countBits(self, n: int) -> List[int]:
        sum=0
        l1=[]
        for i in range(n+1):
            sum=bin(i).count("1")
            l1.append(sum)
        return l1