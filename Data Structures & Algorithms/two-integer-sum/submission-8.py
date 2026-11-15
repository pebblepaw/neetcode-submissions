class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        _remainders = {} 

        for i, num in enumerate(nums): 
            
            remainder = target - num

            print(f'remainder is {remainder}')

            if num in _remainders: 

                index_in_dict = _remainders[num]

                # print(f'i:{i}, index in dict:{index_in_dict}')

                if i < index_in_dict: 
                    return [i, index_in_dict]
                else: 
                    return [index_in_dict, i]
            else: 
                # print('no')
                _remainders[remainder] = i
        
        # print(f'i: {i} num: {num}')
        return "No answer"
  


