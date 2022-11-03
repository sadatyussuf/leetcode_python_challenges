class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not str: return ''
        short = min(strs)
        long = max(strs)
        index = 0
        
        while index < len(short):
            if short[index] != long[index]:
                short = short[:index]
            index += 1
      
        return short