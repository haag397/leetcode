
import re

class Solution:

    def romanToInt(self, s: str) -> int:
        
        if len(s) < 1 or len(s) > 15 :  
            return "length error"    
        
        if re.sub(r'I|V|X|L|C|D|M', '', s):
            return "invali request" 
           
        patterns = r'IV|IX|XL|XC|CD|CM'
        num = 0
        num_2 = 0
        result = re.sub(patterns, '', s)
        for ch in result :
            if ch == "I":
                num = num +1
            if ch == "V":
                num = num +5
            if ch == "X":
                num = num +10
            if ch == "L":
                num = num +50    
            if ch == "C":
                num = num +100
            if ch == "D":
                num = num +500
            if ch == "M":
                num = num +1000    
                
        x = re.findall(patterns, s)
        for n in x: 
            if n == "IV":
                num_2 = num_2 +4
            if n == "IX":
                num_2 = num_2 +9
            if n == "XL":
                num_2 = num_2 +40
            if n == "XC":
                num_2 = num_2 +90    
            if n == "CD":
                num_2 = num_2 +400
            if n == "CM":
                num_2 = num_2 +900

        return num + num_2
  
my_solo = Solution()
print(my_solo.romanToInt("III"))
print(my_solo.romanToInt("LVIII"))
print(my_solo.romanToInt("MCMXCIV"))
print(my_solo.romanToInt(""))
print(my_solo.romanToInt("MCMXCIVaaaaaaaaaaaaa"))
print(my_solo.romanToInt("MCMXCoV"))
print(my_solo.romanToInt("MCMXLIV"))
print(my_solo.romanToInt("MDCLXVI"))
print(my_solo.romanToInt("MMXXIV"))
print(my_solo.romanToInt("MMDCCC"))

