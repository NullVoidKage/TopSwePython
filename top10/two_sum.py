class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the numbers we have seen and their indices
        seen = {}

        # Loop through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement that we need to find in the dictionary
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in seen:
                # If it is, return the indices of the complement and the current number
                return [seen[complement], i]

            # Otherwise, add the current number and its index to the dictionary
            seen[num] = i

        # If no solution is found, return an empty list (though the problem guarantees one solution)
        return []