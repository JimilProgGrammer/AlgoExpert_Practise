# Time: O(N) | Space: O(N)
def waterArea(heights):
    maxes = [0 for x in heights]
    
    # Calculate leftMax
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)
    
    # Calcualate rightMax and at the same time
    # update the amount of water you can store
    # as well
    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        # Minimum of leftMax (stored at maxes[i])
        # and rightMax
        minHeight = min(maxes[i], rightMax)
        # If you can store water at this index, calculate it
        # using the minHeight - height formula
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)
    
    return sum(maxes)
