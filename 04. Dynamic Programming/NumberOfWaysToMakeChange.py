# Time: O(N * d) | Space: O(N)
# where, N -> target amount
#      , d -> length of denominations array
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n+1)]
    # Base Case
    ways[0] = 1
    for denom in denoms:
        for amount in range(1,n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]
