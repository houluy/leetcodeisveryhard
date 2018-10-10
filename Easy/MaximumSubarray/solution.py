def maxSubArray(nums):
    # So complex
    length = len(nums)
    pos_val = {}
    max_val = nums[0]
    for span in range(1, length + 1):
        ind = 0
        while ind <= (length - span):
            s = 0
            for i in range(span):
                s += nums[ind + i]
            if s > max_val:
                max_val = s
            ind += 1
    return max_val

def maxSubArray(nums):
    '''
    maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i]; 
    '''
    length = len(nums)
    max_val = last = nums[0]
    for ind in range(1, length):
        last = nums[ind] + (last if last > 0 else 0)
        if last > max_val:
            max_val = last
    return max_val

nums = [[-2,1,-3,4,-1,2,1,-5,4], [1], [-1]]
for t in nums:
    print(maxSubArray(t))
