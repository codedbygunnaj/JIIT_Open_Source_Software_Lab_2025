# Q10: Find the most repetitive word in a text file
def most_repetitive_word(filename):
    try:
        with open(filename, "r") as f:
            text = f.read().lower().split()
            freq = {}
            for word in text:
                freq[word] = freq.get(word, 0) + 1
            most_word = max(freq, key=freq.get)
            return most_word, freq[most_word]
    except FileNotFoundError:
        return None, 0


# Q11: Return unique elements from list
def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


# Q12: First non-repeating character in string
def first_non_repeating(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None


# Q13: Remove parentheses area in strings
def remove_parenthesis_area(strings):
    result = []
    for s in strings:
        new_s = ""
        inside = False
        for ch in s:
            if ch == "(":
                inside = True
            elif ch == ")":
                inside = False
            elif not inside:
                new_s += ch
        result.append(new_s.strip())
    return result


# ---------------- MAIN ----------------
if __name__ == "__main__":
    # Q10
    word, count = most_repetitive_word("testFile.txt")
    if word:
        print(f"Q10 -> Most repetitive word: '{word}' ({count} times)")
    else:
        print("Q10 -> File not found!")

    # Q11
    lst = [1, 2, 2, 3, 4, 4, 5, 1]
    print("Q11 -> Unique list:", unique_list(lst))

    # Q12
    s = "swiss"
    print("Q12 -> First non-repeating character:", first_non_repeating(s))

    # Q13
    data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
    print("Q13 -> After removing parenthesis area:", remove_parenthesis_area(data))
