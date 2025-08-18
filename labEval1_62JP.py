# Lab Evaluation 1 (All 4 Questions)

# ---------------- EVEN NUMBERED MACHINE ---------------- #

# Q1: Reverse numbers in a linked list using list indexing only
def reverse_linked_list(lst):
    return lst[::-1]


# Q2: Print the mth element from start and mth element from end in a tuple
def print_mth_elements(tpl, m):
    n = len(tpl)
    if m <= 0 or m > n:
        return None, None
    return tpl[m - 1], tpl[-m]


# ---------------- ODD NUMBERED MACHINE ---------------- #

# Q1: Repeat last n characters of string, n times
def repeat_last_n(s, n):
    if n < 0 or n > len(s):
        return ""
    part = s[-n:]  # last n characters
    return part * n


# Q2: Sort hyphen-separated colors alphabetically, uniform case
def sort_colors(seq):
    colors = seq.split('-')
    # Convert all to lowercase for uniformity
    colors = [c.lower() for c in colors]
    colors.sort()
    return '-'.join(colors)


# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    # Even Q1
    lst = [1, 2, 3, 4]
    print("Even Q1 →", reverse_linked_list(lst))

    # Even Q2
    tpl = (10, 20, 30, 40, 50)
    m = 2
    start, end = print_mth_elements(tpl, m)
    print(f"Even Q2 → {m}th from start = {start}, {m}th from end = {end}")

    # Odd Q1
    s = "Jaypee"
    n = 3
    print("Odd Q1 →", repeat_last_n(s, n))

    # Odd Q2
    seq = "green-red-yellow-black-white"
    print("Odd Q2 →", sort_colors(seq))
