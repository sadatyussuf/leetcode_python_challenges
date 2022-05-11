class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_of_s = list(s)
        set_of_s.sort()
        set_of_t = list(t)
        set_of_t.sort()
        
        if len(s) == len(t):
            for item_s,item_t in zip(set_of_s,set_of_t):
                if item_s != item_t:
                    return False
                    return True
                    return False
