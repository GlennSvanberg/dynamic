def can_sum(target, nums, memo={}):
    if target in memo:
        return memo.get(target)
    if target == 0:
        return True
    if target < 0:
        return False
    for num in nums:
        if can_sum(target - num,nums, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False

print(can_sum(800,[4,3,8]))
