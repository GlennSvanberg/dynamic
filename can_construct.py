
def can_construct(target, word_bank):
    if target == "":
        return True
    for word in word_bank:
        n = len(word)
        start_target = target[0:n]
        if start_target == word:
            if can_construct(target[n:], word_bank):
                return True
    return False


print(can_construct("abcdef", ["ab","cd","abc", "defa","efa"]))