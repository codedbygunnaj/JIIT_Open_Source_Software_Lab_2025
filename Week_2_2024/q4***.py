def mutate(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    mutations = set()  # set use kiya taki duplicate na aaye

    # 1. Insert
    for i in range(len(word) + 1):
        for ch in letters:
            mutations.add(word[:i] + ch + word[i:])

    # 2. Delete
    for i in range(len(word)):
        mutations.add(word[:i] + word[i+1:])

    # 3. Replace
    for i in range(len(word)):
        for ch in letters:
            if ch != word[i]:  # same se replace nhi karna
                mutations.add(word[:i] + ch + word[i+1:])

    # 4. Swap
    for i in range(len(word) - 1):
        mutations.add(word[:i] + word[i+1] + word[i] + word[i+2:])

    return mutations


# Example
print(mutate("cat"))



def nearly_equal(a, b):
    return a in mutate(b)


if __name__ == "__main__":
    print(nearly_equal("cat", "bat"))  # True (replace)
    print(nearly_equal("cats", "cat")) # True (insert)
    print(nearly_equal("cta", "cat"))  # True (swap)
    print(nearly_equal("dog", "cat"))  # False
