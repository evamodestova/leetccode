class Solution(object):
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        # idea: transforming x into a string and comparing numbers using indexies of opposite digits
        x_str = str(x)
        # need to use only half of the string, becasue the comparisons further than that were already made (don't needd to compare first and last digits again). using int so that it's a whole number
        for i in range (int(len(x_str)/2)):
            if x_str[i] != x_str[len(x_str)-i-1]:
                # if some compared digits don't match, returning false right away
                return False
        return True
        
    print(isPalindrome(121))
    print(isPalindrome(1211))
# time complexity: O(N)
# runtime: 20 ms    
