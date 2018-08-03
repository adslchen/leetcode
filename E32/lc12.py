class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        value = [1000,900, 500,400, 100, 90, 50, 40, 10, 9, 5,4, 1]
        
        roman = ['M','CM','D', 'CD','C','XC','L','XL','X','IX','V','IV','I']
        
        ans = ""
        i = 0
        while num != 0:
            if num / value[i] >= 1:
                num -= value[i]
                ans += roman[i]
            else:
                i += 1
        return ans
    :
