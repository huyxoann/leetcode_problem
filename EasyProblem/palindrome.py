class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed_string = ''
        for i in str(x):
            reversed_string = i + reversed_string
        return str(x) == reversed_string