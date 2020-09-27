# Solution 1
# Time: O(n ^ 2); Space: O(1)
def twoNumberSum1(array, target):
    for i in range(len(array-1)):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == target:
                return [firstNum, secondNum]
    return []

# Solution 2
# Time: O(n); Space: O(n)
def twoNumberSum2(array, target):
    nums = {}
    for num in array:
        if target - num in nums:
            return [num, target-num]
        else:
            nums[target-num] = True
    return []

# Solution 3
# Time: O(nLog(n)); Space: O(1)
def twoNumberSum3(array, target):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum < target:
            left = left + 1
        elif current_sum > target:
            right = right -1
        elif current_sum == target:
            return [array[left], array[right]]
    return []
