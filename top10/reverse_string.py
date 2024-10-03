class Solution(object):
    def reverseString(self, s):
        """
        Reverses the input list of characters in-place.

        :param s: List[str] - A list of characters
        :return: None - The list is modified in-place
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Swap the characters at the left and right indices
            s[left], s[right] = s[right], s[left]
            # Move the pointers towards the center
            left += 1
            right -= 1