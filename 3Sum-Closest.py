class Solution:
   def threeSumClosest(self, nums: List[int], target: int) -> int:
    # Step 1: Sort the input array to use two-pointer technique
    new_num = sorted(nums)
    
    # Step 2: Initialize the closest sum (answer) with the sum of the first three numbers
    ans = new_num[0] + new_num[1] + new_num[2]
    
    # Step 3: Initialize the minimum difference as a large number (simulate INT_MAX)
    differnce = 2**31 - 1

    # Step 4: Iterate through the array with a fixed first element
    for i in range(len(new_num) - 2):
        num = new_num[i]  # First element of the triplet
        left = i + 1      # Left pointer
        right = len(nums) - 1  # Right pointer

        # Step 5: Apply two-pointer technique to find the best pair with current num
        while left < right:
            sum = num + new_num[left] + new_num[right]  # Current triplet sum

            # Step 6: Update the answer if the current sum is closer to the target
            if abs(sum - target) < differnce:
                differnce = abs(sum - target)
                ans = sum

            # Step 7: Move pointers to try and get closer to the target
            if sum < target:
                left += 1  # Need a larger sum, so move left pointer right
            else:
                right -= 1  # Need a smaller sum, so move right pointer left

    # Step 8: Return the closest sum found
    return ans