def group(mainList,size):
    return [mainList[i:i+size] for i in range(0,len(mainList),size)]

print(group([1,2,3,4,5,6,7,8,9,10],4))