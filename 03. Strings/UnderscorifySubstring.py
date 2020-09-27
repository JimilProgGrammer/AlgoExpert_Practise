# Time: O(N^2 + N * M) time | Space: O(N)
def underscorifySubstring(string, substring):
    locations = collapse(getLocations(string, substring))
    return underscorify(string, locations)

def getLocations(string, substring):
    locations = []
    startIdx = 0
    while startIdx < len(string):
        # Find instance of substring in
        # string[startIdx : len(string)]
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            # New instance of substring found
            locations.append([nextIdx, nextIdx + len(substring)])
            # Next string you want to search for 
            # for the substring
            startIdx = nextIdx + 1
        else:
            # No more traversing required
            break
    return locations

def collapse(locations):
    if not(locations):
        return locations
    newLocations = [locations[0]]
    previous = newLocations[0]
    for i in range(1, len(locations)):
        currentLocation = locations[i]
        if currentLocation[0] <= previous[1]:
            # If current location overlaps with previous location
            previous[1] = currentLocation[1]
        else:
            # If no overlap
            newLocations.append(currentLocation)
            previous = currentLocation
    return newLocations

def underscorify(string, locations):
    locationsIdx = 0
    stringIdx = 0
    inBetweenUnderscores = False
    finalChars = []
    # Whether we are at the start or end of
    # the underscore locations
    i = 0
    while stringIdx < len(string) and locationsIdx < len(locations):
        # If we need to append an underscore at this position
        # in the final string
        if stringIdx == locations[locationsIdx][i]:
            finalChars.append("_")
            inBetweenUnderscores = not inBetweenUnderscores
            if not inBetweenUnderscores:
                locationsIdx += 1
            i = 0 if i == 1 else 1
        # Append current character in final string
        finalChars.append(string[stringIdx])
        stringIdx += 1
    if locationsIdx < len(locations):
        finalChars.append("_")
    elif stringIdx < len(string):
        finalChars.append(string[stringIdx])
    return "".join(finalChars)
