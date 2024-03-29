# Time: O(N) | Space: O(min(N,A))
# where, N -> length of string
#      , A -> length of unique characters in the string
def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    longest = [0, 1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i+1]
        lastSeen[char] = i
    return string[longest[0]:longest[1]]
