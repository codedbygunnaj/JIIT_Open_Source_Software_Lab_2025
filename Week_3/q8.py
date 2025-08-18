def avgMe(l):
    avg = 0.0
    for i in l:
        avg += i
    return avg / len(l)   # FIX: must return

def count_above_average(nums):
    avg = avgMe(nums)
    ans = []
    for i in nums:
        if i > avg:
            ans.append(i)
    return len(ans)   # FIX: must return count, not list
