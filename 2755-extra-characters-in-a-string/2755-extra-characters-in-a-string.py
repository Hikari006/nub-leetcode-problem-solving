class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        cache={}

        def dfs(text):
            if len(text)<=0:
                return 0
            if len(text) in cache:
                return cache[len(text)]
            

            mini=len(text)

            for word in dictionary:
                if text ==word:
                    mini=0
                    cache[len(text)]=mini
                    return mini
                elif text[:len(word)]==word:
                    result=dfs(text[len(word):])
                    mini=min(mini,result)

            mini=min(mini,1+dfs(text[1:]))
            cache[len(text)]=mini
            return mini
        
        return dfs(s)

                
