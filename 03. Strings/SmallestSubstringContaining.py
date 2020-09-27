# Time: O(B + S) | Space: O(B + S)
# where, B -> length of big string
#      , S -> length of small string

# O(S) to build the initial target CharCount hashtable
# O(B) to traverse the string using the sliding window

# O(S) space to store the targetCharCounts hashtable
# O(B) space to store running substringCharCounts hashtable
# in worst case if the bigString == smallString

def smallestSubstringContaining(bigString, smallString):
    targetCharCounts = getCharCounts(smallString)
    substringBounds = getSubstringBounds(bigString, targetCharCounts)
    return getStringFromBounds(bigString, substringBounds)
    
def getCharCounts(string):
    charCounts = {}
    for char in string:
        increaseCharCount(char, charCounts)
    return charCounts
        
def increaseCharCount(char, charCounts):
    if char not in charCounts:
        charCounts[char] = 0
    charCounts[char] += 1
    
def decreaseCharCount(char, charCounts):
    charCounts[char] -= 1

def getSubstringBounds(string, targetCharCounts):
    substringBounds = [0,float("inf")]
    substringCharCounts = {}
    numUniqueChars = len(targetCharCounts.keys())
    numUniqueCharsDone = 0
    leftIdx = 0
    rightIdx = 0
    while rightIdx < len(string):
        rightChar = string[rightIdx]
        # If this character is not to be looked for in the
        # big string, continue
        if rightChar not in targetCharCounts:
            rightIdx += 1
            continue
        # If it is required, increment it's count
        increaseCharCount(rightChar, substringCharCounts)
        # If we have all required instances of this character,
        # increase the number of unique chars done till now
        if substringCharCounts[rightChar] == targetCharCounts[rightChar]:
            numUniqueCharsDone += 1
        
        # Now try contracting the substring from the right by
        # incrementing leftIdx as long as you have the required
        # number of unique characters after contraction
        while numUniqueCharsDone == numUniqueChars and leftIdx <= rightIdx:
            # Check if shorter substring possible
            substringBounds = getCloserBounds(leftIdx, rightIdx, substringBounds[0], substringBounds[1])
            leftChar = string[leftIdx]
            # While contracting, if you find something that is not
            # required from the big string, continue
            if leftChar not in targetCharCounts:
                leftIdx += 1
                continue
            # If you have encountered a character with as many occurences
            # as required while you are contracting, this means that you
            # will be losing one essential character on further contraction
            # So, decrease the number of unique characters done so far and
            # stop the contraction.
            if substringCharCounts[leftChar] == targetCharCounts[leftChar]:
                numUniqueCharsDone -= 1
            # Decrease count of current character in the running charcount
            # hashtable
            decreaseCharCount(leftChar, substringCharCounts)
            # contract from the left
            leftIdx += 1
        # expand to the right
        rightIdx += 1
    return substringBounds

def getCloserBounds(idx1, idx2, idx3, idx4):
    return [idx1, idx2] if idx2-idx1 < idx3-idx4 else [idx3, idx4]

def getStringFromBounds(string, bounds):
    start, end = bounds[0], bounds[1]
    if end == float("inf"):
        return ""
    return string[start:end+1]
