def revOrd(w):
    word=w.split()
    finalAns=""
    for W in word:
        finalAns+=W[::-1]+" "
    return finalAns

print(f"Reverse alpha function of 'hello world python' is {revOrd('hello world python')}")