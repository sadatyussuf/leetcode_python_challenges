class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l_str, s_str =len(str1), len(str2)

        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a % b)
        n_index = gcd(l_str,s_str)

        str1_len_match = str1.count(str1[:n_index])*n_index == l_str
        str2_len_match = str2.count(str1[:n_index])*n_index == s_str

        if (str1[:n_index] == str2[:n_index]) and (str1_len_match and str2_len_match):
            return str1[:n_index]
        return ""
    