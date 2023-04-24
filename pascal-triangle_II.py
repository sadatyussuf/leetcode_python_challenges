# Final Try
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        res = [[1]]

        for i in range(rowIndex):
            temp = [0,*res[-1],0]
            cur_list = list(
                map(lambda x,y:x+y,
                temp[:-1],temp[1:])
                )
            res.append(cur_list)

        return res[rowIndex]

# First Try
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        res = [[1]]
        for i in range(rowIndex):
            temp = [0,*res[-1],0]
            cur_list = []
            for i in range(len(temp)-1):
                cur_list.append(temp[i] + temp[i+1])
            res.append(cur_list)
        print(res)
        return res[rowIndex]