"""
def grid_traveler(a,b):
    if a == 0 or b == 0:
        return 0
    if a == 1 and b  == 1:
        return 1
    return grid_traveler(a-1, b)+ grid_traveler(a, b-1)


print(grid_traveler(1,1))
"""

def grid_traveler(a,b, memo = {}):
    # Are the args in the memo
    key = f"{a},{b}"
    if key in memo:
        return memo.get(key)
    if a == 0 or b == 0:
        return 0
    if a == 1 and b  == 1:
        return 1
    memo[key] = grid_traveler(a-1, b,memo)+ grid_traveler(a, b-1,memo)
    return memo.get(key)


print(grid_traveler(18,18))