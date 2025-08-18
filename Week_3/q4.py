#return nth character
def fun(w,n):
    ans=""
    for i in range(0,len(w),n):
        ans+=w[i]
    return ans

print(f"Return nth function of 'ABCDEFGHIJKLM' for n = 3 is {fun('ABCDEFGHIJKLM',3)}")