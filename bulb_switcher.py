import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        base = 2
        
        if n == 0:
            return 0
        for i in range(0 , 20):
            if n == (2 ** i) - 1:
                return 1
  
        value = math.log(n, base)
        if n % 2 ==0 and value % 2 != 0:
            return 1
        elif n % 2 ==0 and value % 2 == 0:
            return 2

        return 2


sol = Solution()
print("0",sol.bulbSwitch(0))
print('1',sol.bulbSwitch(1))
print('2',sol.bulbSwitch(2))
print('3',sol.bulbSwitch(3))
print('4',sol.bulbSwitch(4))
print('5',sol.bulbSwitch(5))
