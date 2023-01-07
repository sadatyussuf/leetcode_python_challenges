class Solution:
    def addBinary(self, a: str, b: str) -> str:

        len_str_a = len(a) -1
        len_str_b = len(b) -1
        decimal_a = 0
        decimal_b = 0
        decimal_total = 0
        binary_str = ''
        
        # converting from the binary string to decimals
        for i in a:
            decimal_a += ( int(i) * 2**len_str_a)
            len_str_a -=1
        for i in b:
            decimal_b += ( int(i) * 2**len_str_b)
            len_str_b -=1
        # sum the two decimals
        decimal_total = decimal_a + decimal_b 
        if decimal_total == 0:
            return '0'
            
        while decimal_total > 0:
            if decimal_total % 2  == 0:
                # binary_str += '0'
                binary_str = '0' + binary_str
            else:
                # binary_str += '1'
                binary_str = '1' + binary_str
            print(decimal_total,decimal_total % 2)
            decimal_total = decimal_total // 2

        
        return binary_str
