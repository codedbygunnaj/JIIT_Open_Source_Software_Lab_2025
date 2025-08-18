def triplet(n):
    triplets = set()   # to avoid duplicates like (a,b,c) and (b,a,c)
    for a in range(1, n):
        for b in range(a, n):  # start from 'a' so (a,b) and (b,a) don’t repeat
            c = a + b
            if c < n:   # c should also be less than n
                triplets.add((a, b, c))  
    return list(triplets)


if __name__ == "__main__":
    # n = int(input("Enter a number: "))
    n=10
    result = triplet(n)
    print("Triplets are:")
    for t in result:
        print(t)
    print()
    print()
    print()


def trip(n):
    triplets = []
    for c in range(1, n):           # c < n
        for a in range(1, c):       # a < c
            b = c - a
            if b > 0 and b < n:     # valid number
                t = (min(a,b), max(a,b), c)   # sorted to avoid (a,b) and (b,a)
                if t not in triplets:
                    triplets.append(t)
    return triplets

# Example
print(trip(10))
