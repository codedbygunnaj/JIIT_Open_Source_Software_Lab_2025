#Anagrams: When 2 words are equal by alphabet count and same made of same alphabets.
def make_dic(word):
    d={}
    for w in word:
        # if d[w] in d:
        #     d[w]+=1
        # else:
        #     d[w]=1
        d[w]=d.get(w,0)+1
    return d

def are_anagrams(w1, w2):
    return make_dic(w1)==make_dic(w2)

print(are_anagrams("eat", "tea"))   # True
print(are_anagrams("bat", "tab"))   # True
print(are_anagrams("cat", "dog"))   # False