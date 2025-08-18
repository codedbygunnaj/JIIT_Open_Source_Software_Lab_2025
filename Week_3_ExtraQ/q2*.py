# def lenSort(list):
#     #can apply bubbleSort for sorting according to length, if length is equal then we can go for ascii coding
def lenSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(lst[j]) > len(lst[j+1]) or (len(lst[j]) == len(lst[j+1]) and lst[j] > lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


# def extSort(list):
#     #similar logic as of lenSort()


# best is lambda logic which we can apply in list for sorting:
def lenSort(list):
    return sorted(lst,key=lambda x: (len(x),x)