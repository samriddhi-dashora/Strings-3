# TC: O(1) - max it will run is number of digiuts times which is the range of integers which is finite
# SC: O(1) - all the arrays are created beforehand and are fixed length, the recursive stack at a time can have 3 digits
'''
Define arrays to hold the words for numbers less than twenty, tens, and powers of a thousand
Helper function to convert a number less than 1000 into words
    If the number is less than 20, directly map it to its word representation
    If the number is less than 100, convert the tens place and recursively convert the remainder
    If the number is less than 100, convert the tens place and recursively convert the remainder

Process each group of three digits (thousands, millions, billions)
If the current group is not zero, convert it to words and add the appropriate power of a thousand
Return the final result string with leading/trailing spaces removed
'''



class Solution(object):
    BELOW_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",         "Nineteen"    ]
    TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def helper(self, num):
        if num == 0:
            return ""
        elif num <20:
            return self.BELOW_20[num] + " "
        elif num < 100:
            return self.TENS[num//10]+ " " + self.helper(num % 10)
        else:
            return self.BELOW_20[num//100] + " Hundred " + self.helper(num%100)

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        if num == 0:
            return "Zero"

        i = 0 #index on thousands array
        words = ""

        while(num>0):
            if num%1000 !=0:
                words = self.helper(num%1000) + self.THOUSANDS[i] + " " + words
            num//=1000
            i +=1
        
        return words.strip()


        