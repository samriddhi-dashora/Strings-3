######### using Calc and tail vars ############
# TC : O(n) SC: O(1)
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        calc = 0  #This will hold the cumulative result
        num = 0  # This will hold the current number being processed
        prev_op = '+'  # The last operator seen, starting with '+'
        tail = 0  # This is used for correctly handling '*' and '/' operations

        for i in range(len(s)):
            char = s[i]
            if char.isdigit(): # If the character is a digit, build the number
                num = num*10 + int(char)
                #print(num)

            if not char.isdigit() and char !=' ' or i == len(s)-1:
                if prev_op =='+':
                     calc += num
                     tail = num
                elif prev_op == '-':
                    calc -= num
                    tail = -num
                    #print("second")
                elif prev_op == '*':
                    calc = calc - tail + tail * num
                    tail = tail * num
                elif prev_op == '/':
                    print(tail)
                    print(tail//num)
                    calc = calc - tail + int(tail/num)
                    tail = int(tail / num)
                    #print("my curr", calc, tail)
                #print(calc)
                print("calc", calc)
                print("tail", tail)
                prev_op = char
                num = 0
        return calc 

######### USING STACK ###############
# TC : O(n) SC: O(n)
'''
Keep traversing over the sring and calc the number, if it is an operator like + or - , keep pushing to the stack
if the operator is * or /, then it needs ot be resolved first before pushing
handle the egde case of char != ' ' and if it is the last element
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0

        prev_op = '+'

        for i in range(len(s)):
            char = s[i]

            if char.isdigit():
                num = num*10 + int(char)
            if not char.isdigit() and char !=' ' or i == len(s)-1:
                if prev_op =='+':
                     stack.append(+num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                elif prev_op == '/':
                    stack.append(int(stack.pop())//num)
                num = 0
                prev_op = char
        return sum(stack)