def ctMe(s):
    strNew = ""
    d = {}
    for ch in s:
        if ch.islower():
            d['lower'] = d.get('lower', 0) + 1
            strNew += ch.upper()
        else:
            d['upper'] = d.get('upper', 0) + 1
            strNew += ch.lower()
    return d, strNew

print(ctMe("HeLLo"))
# ({'upper': 3, 'lower': 2}, 'hEllO')


def toggle_case_count(s):
    counts = {"upper": sum(1 for ch in s if ch.isupper()),
              "lower": sum(1 for ch in s if ch.islower())}
    return counts, s.swapcase()
#GOOOOOOD WAYYYYYYY