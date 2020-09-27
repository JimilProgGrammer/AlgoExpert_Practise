# Time: O(N) where N = n*n; Space: O(N)
def spiralTraverse(array):
    result = []
    startRow, endRow, startCol, endCol =  0,0,len(array)-1,len(array[0])-1
    
    while startRow <= endRow and startCol <= endCol:
        # Traverse top border
        for col in range(startCol, endCol+1):
            result.append(array[startRow][col])
            
        # Traverse right border
        for row in range(startRow+1,endRow+1):
            result.append(array[row][endCol])
        
        # Traverse bottom border
        for col in reversed(range(startCol,endCol)):
            result.append(array[endRow][col])
        
        # Traverse left border
        for row in reversed(range(startRow+1,endRow)):
            result.append(array[row][startCol])
        
        startRow = startRow + 1
        startCol = startCol + 1
        endRow = endRow - 1
        endCol = endCol - 1
    return array

# Time: O(N) where N = n*n; Space: O(N)
def spiralTraverseRecursive(array):
    result = []
    spiralFill(array, 0, len(array)-1, 0, len(array[0])-1, result)
    return result

# Recursive helper
def spiralFill(array, startRow, endRow, startCol, endCol, result):
    if startRow > endRow or startCol > endCol:
        return 

    # Traverse top border
    for col in range(startCol, endCol+1):
        result.append(array[startRow][col])
        
    # Traverse right border
    for row in range(startRow+1,endRow+1):
        result.append(array[row][endCol])
    
    # Traverse bottom border
    for col in reversed(range(startCol,endCol)):
        result.append(array[endRow][col])
    
    # Traverse left border
    for row in reversed(range(startRow+1,endRow)):
        result.append(array[row][startCol])
    
    spiralFill(array, startRow+1, endRow-1, startCol+1, endCol-1, result)
