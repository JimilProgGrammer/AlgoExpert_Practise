# Time: O(N^2) | Space: O(1)
def longestPalindromicSubstring(string):
    currentLongest = [0,1]
    for i in range(1, len(string)):
        # Checking for an odd-length palindrome
        # centred at string[i]
        odd = getLongestPalindromeFrom(string, i-1, i+1)
        # Checking for an even-length palindrome
        # centred between string[i-1] and string[i]
        even = getLongestPalindromeFrom(string, i-1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]
    
def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    # leftIdx + 1 cause at this point, leftIdx is 1 position 
    # left to actual starting index
    # rightIdx is also one position to the right but we want 
    # that because that acts as our exclusive index when we 
    # finally substring
    return [leftIdx+1, rightIdx]
