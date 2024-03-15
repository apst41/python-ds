class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        if n == 2: return '11'
        input_str = '11'
        
        for i in range(3, n + 1):
            input_str += '$'
            tmp = ""
            count = 1
            for j in range(1, len(input_str)):
                if input_str[j] != input_str[j - 1]:
                    tmp += str(count) + input_str[j - 1]
                    count = 1
                else:
                    count += 1
            
            input_str = tmp
        return input_str
