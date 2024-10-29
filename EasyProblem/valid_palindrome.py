class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        filtered_string = ''.join(char for char in s if char.isalnum()).lower()
        
        return filtered_string == filtered_string[::-1]