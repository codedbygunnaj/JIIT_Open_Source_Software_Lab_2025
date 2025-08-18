#all unique or not:
def unq(w):
    w=w.lower()
    return (len(set(w)))==len(w)

print(f"Unique alpha function of 'GunajChugh' is {unq('GunajChugh')}")
print(f"Unique alpha function of 'ABCDEFGHIJKL' is {unq('ABCDEFGHIJKL')}")