def change(w):
    if len(w)<=2:
        return w
    return w[0]+"*"*(len(w)-2)+w[-1] #w[len(w)-1]

print(f"Star function of 'GunajChugh' is {change('GunajChugh')}")