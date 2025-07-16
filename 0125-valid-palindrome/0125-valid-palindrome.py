class Solution:
    def isPalindrome(self, s: str):
        # Initialize an empty list to store alphanumeric characters
        filtered_chars = []

        # Iterate over each character in the string
        for char in s:
            if char.isalnum():  # Check if the character is alphanumeric
                filtered_chars.append(char.lower())  # Add lowercase version to the list

        # Check if the filtered list of characters is the same forward and backward
        return filtered_chars == filtered_chars[::-1]