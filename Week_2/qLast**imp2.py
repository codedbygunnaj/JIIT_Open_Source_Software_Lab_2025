import ./'qLast**imp.py'
words = ["eat", "ate", "tea", "bat", "tab", "tan"]

groups = []
while words:
    word = words.pop()
    group = [word]
    for other in words[:]:  # copy of list
        if are_anagrams(word, other):
            group.append(other)
            words.remove(other)
    groups.append(group)

print(groups)


[['tan'], ['bat', 'tab'], ['eat', 'ate', 'tea']]
