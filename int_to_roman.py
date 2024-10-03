import re

class Solution:
    def intToRoman(self, num: int) -> str:
        digits = re.findall(r'\d', str(num))
        result = []
        if 1000 <= num < 3999 :
            num_M = int(digits[0])
            result.append(num_M*"M")
            
            if 1 <= int(digits[1]) <= 3:
                num_C = int(digits[1])
                result.append(num_C*"C")
            elif int(digits[1]) == 4:
                result.append("CD")
            elif int(digits[1]) == 5:
                result.append("D")
            elif 6 <= int(digits[1]) <= 8:
                num_C = int(digits[1]) - 5
                result.append("D")
                result.append(num_C*"C")
            elif int(digits[1]) == 9:
                result.append("CM")   
                
            if 1 <= int(digits[2]) <= 3:
                num_X = int(digits[2])
                result.append(num_X*"X")
            elif int(digits[2]) == 4:
                result.append("XL")

            elif int(digits[2]) == 5:
                result.append("L")

            elif 6 <= int(digits[2]) <= 8:
                num_C = int(digits[2]) - 5
                result.append("L")
                result.append(num_C*"X")

            elif int(digits[2]) == 9:
                result.append("XC")
            if 1 <= int(digits[3]) <= 3:
                num_I = int(digits[3])
                result.append(num_I*"I")                
            elif int(digits[3]) == 4:
                result.append("IV")
            elif int(digits[3]) == 5:
                result.append("V")
            elif 6 <= int(digits[3]) <= 8:
                num_I = int(digits[3]) - 5
                result.append("V")
                result.append(num_I*"I")
            elif int(digits[3]) == 9:
                result.append("IX")       
                
        if 100 <= num < 1000 :
            if 1 <= int(digits[0]) <= 3:
                num_C = int(digits[0])
                result.append(num_C*"C")
            elif int(digits[0]) == 4:
                result.append("CD")
            elif int(digits[0]) == 5:
                result.append("D")
            elif 6 <= int(digits[0]) <= 8:
                num_C = int(digits[0]) - 5
                result.append("0")
                result.append(num_C*"C")
            elif int(digits[0]) == 9:
                result.append("CM")   
                
            if 1 <= int(digits[1]) <= 3:
                num_X = int(digits[1])
                result.append(num_X*"X")
            elif int(digits[1]) == 4:
                result.append("XL")
            elif int(digits[1]) == 5:
                result.append("L")
            elif 6 <= int(digits[1]) <= 8:
                num_C = int(digits[1]) - 5
                result.append("L")
                result.append(num_C*"X")
            elif int(digits[1]) == 9:
                result.append("XC")    

            if 1 <= int(digits[2]) <= 3:
                num_I = int(digits[2])
                result.append(num_I*"I")
            elif int(digits[2]) == 4:
                result.append("IV")
            elif int(digits[2]) == 5:
                result.append("V")
            elif 6 <= int(digits[2]) <= 8:
                num_I = int(digits[2]) - 5
                result.append("V")
                result.append(num_I*"I")
            elif int(digits[2]) == 9:
                result.append("IX")      
                
        if 10 <= num < 100 :
            if 1 <= int(digits[0]) <= 3:
                num_X = int(digits[0])
                result.append(num_X*"X")
            elif int(digits[0]) == 4:
                result.append("XL")
            elif int(digits[0]) == 5:
                result.append("L")
            elif 6 <= int(digits[0]) <= 8:
                num_C = int(digits[0]) - 5
                result.append("L")
                result.append(num_C*"X")
            elif int(digits[0]) == 9:
                result.append("XC")    
                
            if 1 <= int(digits[1]) <= 3:
                num_I = int(digits[1])
                result.append(num_I*"I")
            elif int(digits[1]) == 4:
                result.append("IV")
            elif int(digits[1]) == 5:
                result.append("V")
            elif 6 <= int(digits[1]) <= 8:
                num_I = int(digits[1]) - 5
                result.append("V")
                result.append(num_I*"I")
            elif int(digits[1]) == 9:
                result.append("IX")      
                
        if 0 < num <= 10 :
    
            if 1 <= int(digits[0]) <= 3:
                num_I = int(digits[0])
                result.append(num_I*"I")
            elif int(digits[0]) == 4:
                result.append("IV")
            elif int(digits[0]) == 5:
                result.append("V")
            elif 6 <= int(digits[0]) <= 8:
                num_I = int(digits[0]) - 5
                result.append("V")
                result.append(num_I*"I")
            elif int(digits[0]) == 9:
                result.append("IX")      
                                
        final_result = ''.join(result)
        print(f'"{final_result}"')

sol = Solution()
sol.intToRoman(3749)
