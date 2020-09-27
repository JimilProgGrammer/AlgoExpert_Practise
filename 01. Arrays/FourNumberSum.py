# Time: O(N^2) on avg, O(N^3) worst; Space: O(N^2)
def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = []
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            currentSum = array[i] + array[j]
            diff = targetSum - currentSum
            if diff in allPairSums:
                for pair in allPairSums[diff]:
                    quadruplets.append(pair + [array[i], array[j]])
        
        for j in range(0,i):
            currentSum = array[i] + array[j]
            if currentSum is not in allPairSums:
                allPairSums[currentSum] = [[array[j],array[i]]]
            else:
                allPairSums[currentSum].append([array[j],array[i]])
    return quadruplets