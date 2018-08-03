class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0 : return "Zero"
        self.number = ["","One","Two","Three",'Four','Five',"Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        
       
        thousand = ["","Thousand","Million","Billion"]
        i = 0
        word = ""
        while num != 0:
            
            if (num % 1000) != 0:
                word = self.helper(num%1000) + thousand[i] + " " + word
            
            num /= 1000
            i += 1
            
        return word.strip()
        
        
        
    def helper(self, n):
        if n == 0:
            return ""
        elif n < 20:
            return self.number[n] + " "
        elif n < 100:
            return self.tens[n/10] + " " + self.helper(n%10)
        else:
            return self.number[n/100] + " Hundred " + self.helper(n%100)
