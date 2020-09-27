# O(n^2) time | O(n) space [to store the triplets]
def threeNumberSum(array, target):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currSum = array[i] + array[left] + array[right]
            if currSum == target:
                triplets.append([array[i],array[left],array[right]])
                left += 1
                right -= 1
            elif currSum < target:
                left += 1
            elif currSum > target:
                right -= 1
    return triplets
