class Solution:
    def compress(self, chars: List[str]) -> int:
        c = 1
        hd = 0
        if len(chars) == 1: return len(chars)
        for i in range(len(chars)):
            if i == 0:
                prev = chars[i]
            elif prev == chars[i]:
                c += 1
            else:
                if c == 1:
                    hd += 1
                    chars[hd] = chars[i]
                    prev = chars[i]
                if c > 1:
                    if c > 9:
                        s = list(str(c))
                        for j in s:
                            hd += 1
                            chars[hd] = j                        
                    else:               
                        hd += 1
                        chars[hd] = str(c)
                    hd += 1
                    chars[hd] = chars[i]
                    prev = chars[i]
                    c = 1
        else:       
            if c > 1:            
                if c > 9:
                    s = list(str(c))
                    for i in s:
                        hd += 1
                        chars[hd] = i
                else:               
                    hd += 1
                    chars[hd] = str(c)

        
        return len(chars[:hd+1])



