# Time: O(N^2) | Space: O(N)
# where, N -> length of disks
def diskStacking(disks):
    disks.sort(key=lambda disk: disk[2])
    heights = [x[2] for x in disks]
    sequences = [None for disk in disks]
    maxHeightsIdx = 0
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(0, i):
            otherDisk = disks[j]
            if areValidDimensions(otherDisk, currentDisk):
                if heights[i] <= currentDisk[2] + heights[j]:
                    heights[i] = currentDisk[2] + heights[j]
                    sequences[i] = j
        if heights[i] >= heights[maxHeightsIdx]:
            maxHeightsIdx = i
    return buildSequence(disks, sequences, maxHeightsIdx)
  
def areValidDimensions(otherDisk, currentDisk):
    return otherDisk[0] < currentDisk[0] and otherDisk[1] < currentDisk[1] and otherDisk[2] < currentDisk[2]

def buildSequence(disks, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(disks[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))
