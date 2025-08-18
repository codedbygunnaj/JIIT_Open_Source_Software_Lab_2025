#longest Word:
def lword(tx):
    word=tx.split()
    lw=""
    for w in word:
        if len(w)>len(lw):
            lw=w
    return lw

print(f"Longest word in string 'Hey , myself Gunaj Chugh' is {lword("Hey, myself Gunaj Chugh")}")