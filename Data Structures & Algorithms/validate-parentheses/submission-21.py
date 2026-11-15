class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        _dict = {')':'(', ']':'[', '}':'{'}

        for ch in s: 
            print(ch)

            if ch in _dict:
                if not stack or (stack[-1] != _dict[ch]):
            
                    return False
                stack.pop()

            if ch in _dict.values(): 
                stack.append(ch)
               
        return len(stack)==0