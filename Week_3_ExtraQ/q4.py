def file_stats(filePath):
    with open(filePath, "r") as f:
        lines = f.readlines()
    
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)

    return num_lines, num_words, num_chars


# Example
lines, words, chars = file_stats("sample.txt")
print("Lines:", lines)
print("Words:", words)
print("Characters:", chars)
