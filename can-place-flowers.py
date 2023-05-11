class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        n_of_flower = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n_of_flower +=1 
            return n_of_flower >= n
        

        for i,bed in enumerate(flowerbed):
            if i == 0 :
                if bed == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n_of_flower += 1
                # print('first')
            elif i == len(flowerbed)-1:
                if bed == 0 and flowerbed[i-1] == 0:
                     flowerbed[i] = 1
                     n_of_flower += 1
                # print('last')
            else:
                if bed == 0 and flowerbed[i+1] == 0and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n_of_flower += 1
                print(i,bed)

            
        return n_of_flower >= n