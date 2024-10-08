class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Create a filtered version of the string with only alphanumeric characters in lowercase
        filtered_chars = [char.lower() for char in s if char.isalnum()]

        # Check if the filtered list of characters is equal to its reverse
        return filtered_chars == filtered_chars[::-1]