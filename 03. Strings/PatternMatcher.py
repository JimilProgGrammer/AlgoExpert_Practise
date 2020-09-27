# Time: O(N*2 + M) | Space: O(N + M)
def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []
    newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]
    counts = {"x": 0, "y": 0}
    firstYPos = getCountsAndFirstYPos(newPattern, counts)
    if counts['y'] != 0:
        for lenOfX in range(1, len(string)):
            lenOfY = (len(string) - lenOfX*counts['x']) / counts['y']
            # length of y cannot be negative or a decimal number
            if lenOfY <= 0 or lenOfY % 1 != 0:
                continue
            lenOfY = int(lenOfY)
            yIdx = firstYPos * lenOfX
            potentialX = string[0 : lenOfX]
            potentialY = string[yIdx : yIdx+lenOfY]
            potentialMatch = map(lambda char: potentialX if char == "x" else potentialY, newPattern)
            if "".join(potentialMatch) == string:
                return [potentialX, potentialY] if not didSwitch else [potentialY, potentialX]
    else:
        lenOfX = len(string)/counts['x']
        if lenOfX % 1 == 0:
            lenOfX = int(lenOfX)
            potentialX = string[:lenOfX]
            potentialMatch = map(lambda char: potentialX, newPattern)
            if "".join(potentialMatch) == string:
                return [potentialX, ""] if not didSwitch else ["", potentialX]
    return []

def getNewPattern(pattern):
    patternLetters = list(pattern)
    if pattern[0] == "x":
        return patternLetters
    else:
        return list(map(lambda char: "x" if char == "y" else "y", patternLetters))

def getCountsAndFirstYPos(pattern, counts):
    firstYPos = None
    for i, char in enumerate(pattern):
        counts[char] += 1
        if char == "y" and firstYPos is None:
            firstYPos = i
    return firstYPos
