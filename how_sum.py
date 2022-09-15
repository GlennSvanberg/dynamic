# targetsum, array of numbers. all possible combinations 
"""
def how_sum(target,nums):
    if target < 0:
        return None
    if target == 0:
        return []
    for num in nums:
        res = how_sum(target - num, nums)
        if res != None:
            res.append(num)
            return res
    return None

print(how_sum(7,[1,3]))
"""
def how_sum(target,nums,memo={}):
    if target in memo:
        return memo.get(target)
    if target < 0:
        return None
    if target == 0:
        return []
    for num in nums:
        res = how_sum(target - num, nums)
        if res != None:
            res.append(num)
            memo[target] = res
            return res
    memo[target] = None
    return None

print(how_sum(300,[7,13]))