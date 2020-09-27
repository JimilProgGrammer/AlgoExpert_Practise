# Time: O(N * M^2 + N*log(N)) | Space: O(N*M)
# where, N -> length of the input array of strings
#      , M -> length of longest string
def longestStringChain(strings):
    stringChains = {}
    for string in strings:
        stringChains[string] = {"nextString": "", "maxChainLength":1}
    
    sortedStrings = sorted(strings, key=len)
    for string in sortedStrings:
        findLongestStringChain(string, stringChains)
    return buildLongestStringChain(strings, stringChains)

def findLongestStringChain(string, stringChains):
    for i in range(len(string)):
        smallerString = getSmallerString(string, i)
        if smallerString not in stringChains:
            continue
        tryUpdateLongestStringChain(string, smallerString, stringChains)
    
def getSmallerString(string, i):
    return string[0:i] + string[i+1:]

def tryUpdateLongestStringChain(currentString, smallerString, stringChains):
    smallerStringChainLength = stringChains[smallerString]['maxChainLength']
    currentStringChainLength = stringChains[currentString]['maxChainLength']
    if smallerStringChainLength+1 > currentStringChainLength:
        stringChains[currentString]["maxChainLength"] = smallerStringChainLength + 1
        stringChains[currentString]["nextString"] = smallerString

def buildLongestStringChain(strings, stringChains):
    maxChainLength = 0
    chainStartingString = 0
    for string in strings:
        if stringChains[string]["maxChainLength"] > maxChainLength:
            maxChainLength = stringChains[string]["maxChainLength"]
            chainStartingString = string
            
    result = [chainStartingString]
    currentString = chainStartingString
    while currentString != "":
        result.append(currentString)
        currentString = stringChains[currentString]["nextString"]
    return [] if len(result )== 1 else result
