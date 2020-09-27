# Time: O(N^2) | Space: O(N)
def isPalindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString

# Time: O(N) | Space: O(N)
def isPalindrome1(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)

# Time: O(N) | Space: O(N)
def isPalindrome2(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome2(string, i+1)

# Time: O(N) | Space: O(1)
def isPalindrome3(string):
    left = 0
    right = len(string - 1)
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True