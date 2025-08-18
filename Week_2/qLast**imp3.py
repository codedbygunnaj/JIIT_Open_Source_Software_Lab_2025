def are_anagrams(w1, w2):
    return sorted(w1) == sorted(w2)

# Test
print(are_anagrams("eat", "tea"))   # True
print(are_anagrams("bat", "tab"))   # True
print(are_anagrams("cat", "dog"))   # False


words = ["eat", "ate", "tea", "bat", "tab", "tan"]

anagram_groups = {}
for w in words:
    key = "".join(sorted(w))   # same key for all anagrams
    anagram_groups.setdefault(key, []).append(w)

print(list(anagram_groups.values()))
