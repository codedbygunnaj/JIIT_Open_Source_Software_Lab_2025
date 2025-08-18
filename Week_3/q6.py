#Compressor:
# "aaabbccccd" → Output: "a3b2c4d1"

def unq(w):
    order=""
    d={}
    for i in w:
        d[i]=d.get(i,0)+1
    for k,v in d.items():
        order+=f"{k}{v}"
    return order

print(f"Unique code function of 'aaabbccccd' is {unq('aaabbccccd')}")