def remove_element(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    ind = 0
    max_ind = len(nums) - 1
    while ind <= max_ind:
        if nums[ind] == val:
            if ind == max_ind:
                return ind
            nums[ind], nums[max_ind] = nums[max_ind], nums[ind]
            max_ind -= 1
        else:
            ind += 1
    return ind

