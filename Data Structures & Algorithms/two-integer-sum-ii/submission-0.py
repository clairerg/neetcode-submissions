
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(numbers)):
            dct[numbers[i]] = i+1
        
        print(dct)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in dct:
                return [i+1, dct[diff]]

        