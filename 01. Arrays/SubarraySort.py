# Time: O(N); Space: O(1)
def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    
    # find min and max unsorted
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    
    # base case
    if minOutOfOrder == float("inf"):
        return [-1,-1]
    
    # find start and end of smallest subarray
    subarrayLeftIdx = 0
    while minOutOfOrder >= array[subarrayLeftIdx]:
        subarrayLeftIdx += 1    
    subarrayRightIdx = len(array) - 1
    while maxOutOfOrder <= array[subarrayRightIdx]:
        subarrayRightIdx -= 1
    return [subarrayLeftIdx, subarrayRightIdx]
    
def isOutOfOrder(i, num, array):
    # first element is out of order if it's greater than 2nd element
    if i == 0:
        return num > array[i+1]
    # last element is out of order if it's lesser than the 2nd to last element
    if i == len(array)-1:
        return num < array[i-1]
    # all other elements are out of order if they're smaller than prev or greater than next
    return num > array[i+1] or num < array[i-1]
