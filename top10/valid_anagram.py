class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If the lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Create dictionaries to count the frequency of each character in both strings
        count_s = {}
        count_t = {}

        # Count the frequency of characters in s
        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1

        # Count the frequency of characters in t
        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1

        # Compare the two dictionaries
        return count_s == count_t