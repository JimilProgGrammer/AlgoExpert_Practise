# Approach 1: Time: O(B^2 * R); Space: O(B)
def apartmentHunting(blocks, reqs):
    maxDistancesAtBlocks = [float("-inf") for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            closestReqDistance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, distanceBetween(i,j))
            maxDistancesAtBlocks[i] = max(closestReqDistance, maxDistancesAtBlocks[i])
    return getIndexAtMinValue(maxDistancesAtBlocks)

def getIndexAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue

def distanceBetween(i, j):
    return abs(i - j)

# Approach 2: Time: O(B*R); Space: O(B*R)
def apartmentHunting1(blocks, reqs):
    # Space: O(B * R)
    minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs)) # O(B * R)
    # Space: O(B)
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks) # O(B * R)
    return getIndexAtMinValue(maxDistancesAtBlocks) # O(B)
    
# Time: O(B)
def getMinDistances(blocks, req): 
    minDistances = [0 for block in blocks]
    closestReqIdx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = distanceBetween(i, closestReqIdx)        
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))
    return minDistances

# Time: O(B*R)
def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
    maxDistancesAtBlocks = [0 for block in blocks]
    for i in range(len(blocks)): # O(B)
        # Assume minDistancesFromBlocks is:
        # [0, 0, 1, 1, 0]
        # [2, 3, 1, 0, 0]
        # [0, 4, 1, 2, 0]
        
        # Output from the below line will be:
        # minDistancesAtBlocks[0] = [0,2,0]
        # minDistancesAtBlocks[1] = [0,3,4]
        # and so on and so forth
        minDistancesAtBlocks = list(map(lambda distances: distances[i], minDistancesFromBlocks)) # O(R)
        maxDistancesAtBlocks[i] = max(minDistancesAtBlocks)
    return maxDistancesAtBlocks
