def best_sum(target,nums, memo={}):
    if target in memo:
        return memo.get(target).copy()
    if target < 0:
        return None
    if target == 0:
        return []
    shortest = None
    for num in nums:
        res = best_sum(target - num, nums,memo)
        if res != None:
            res.append(num)
            if shortest == None or len(shortest) > len(res):
                shortest = res.copy()
    memo[target] = shortest
    return shortest.copy()

print(best_sum(100,[1,2,5,25]))
#print(best_sum(26,[3,4,5]))