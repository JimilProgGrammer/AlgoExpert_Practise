# Solution 1: Naive Approach
# Time: O(N^2); Space: O(N)
def minRewards1(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        j = i-1
        # If current score is greater than previous one
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        # If current score is lesser than previous one
        else:
            # Roll backwards till you have a previous greater score
            # Fix reward for each of those scores
            while j >= 0 and scores[j] > scores[j+1]:
                rewards[j] = max(rewards[j], rewards[j+1]  + 1)
                j -= 1
    return sum(rewards)

# Solution 2: Use local mins and maxes
# Time: O(N); Space: O(N)
def minRewards2(scores):
    rewards = [1 for _ in scores]
    localMinIdxs = getLocalMinIdxs(scores)
    for localMinIdx in localMinIdxs:
        expandFromLocalMinIdx(localMinIdx, scores, rewards)
    return sum(rewards)

def expandFromLocalMinIdx(localMinIdx, scores, rewards):
    # Expand to the left until you reach a peak (up to down from left to right)
    leftIdx = localMinIdx - 1
    while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
        rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx+1]+1)
        leftIdx -= 1
    # Expand to the right until you reach a peak (down to up from left to right)
    rightIdx = localMinIdx + 1
    while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1]:
        # Don't need to apply max check here since at this point
        # you'll never be overwriting any value
        rewards[rightIdx] = rewards[rightIdx - 1] + 1

def getLocalMinIdxs(scores):
    if len(scores)==1:
        return 0
    localMinIdxs = []
    for i in range(len(scores)):
        if i == 0 and scores[i] < scores[i+1]:
            localMinIdxs.append(i)
        if i == len(scores)-1 and scores[i] < scores[i-1]:
            localMinIdxs.append(i)
        if i == 0 or i == len(scores)-1:
            continue
        if scores[i] < scores[i+1] and scores[i] < scores[i-1]:
            localMinIdxs.append(i)
    return localMinIdxs

# Solution 3: Use simple traversal
# Time: O(N); Space: O(N)
def minRewards3(scores):
    rewards = [1 for _ in scores]
    # Traverse from left tp right
    for i in range(1, len(scores)):
        # if you are in an upward trend
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1]+1
    # Traverse from right to left
    for i in reversed(range(0, len(scores)-1)):
        # if you are in an upward trend from right to left 
        if scores[i] > scores[i+1]:
            rewards[i] = max(rewards[i], rewards[i+1]+1)
    return sum(rewards)
