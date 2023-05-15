
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        hd = 0
        tail = len(s) -1   
        
        while hd < tail:
            if s[hd].lower() in vowels and s[tail].lower() in vowels:
                s[hd],s[tail] = s[tail], s[hd]
                hd +=1
                tail -=1
            if s[hd].lower() not in vowels:
                hd +=1
            if s[tail].lower() not in vowels:
                tail -=1

        s = "".join(s)
        return s
