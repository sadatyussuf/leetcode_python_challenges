class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        c1 = 0
        min_word = min(len(word1),len(word2))
        res = ""

        while c1 <= min_word-1:
            res += word1[c1]
            res += word2[c1]
            c1+=1
        if c1 < len(word1):
            res += word1[c1:]
        else:
            res += word2[c1:]
   
        return res
