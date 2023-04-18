
# Thrird Optimization
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for row in range(numRows-1):
            temp_list=[0,*res[-1],0]  
            cur_list = list(map(lambda x,y:x+y , 
                                temp_list[:-1],
                                temp_list[1:]))

            res.append(cur_list)
        return res




# Second Try

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for row in range(numRows-1):
            temp_list=[0,*res[-1],0]
            cur_list = []     
            for i in range(len(temp_list)-1):
                temp_sum = temp_list[i] + temp_list[i+1]
                cur_list.append(temp_sum)
            res.append(cur_list)
        return res






# First Try 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for row in range(numRows):
            if not res:
                res.append([1])
            else:
                if len(res) == 1:
                    res.append([1,1])
                else:
                    temp_list=[0,*res[-1],0]
                    cur_list = []
                    for i in range(len(temp_list)-1):
                        temp_sum = temp_list[i] + temp_list[i+1]
                        cur_list.append(temp_sum)
                    res.append(cur_list)
        return res