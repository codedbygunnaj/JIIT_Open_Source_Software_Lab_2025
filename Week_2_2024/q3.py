def parse_csv(filename):
    data = []
    with open(filename, "r") as f:
        content = f.read().strip()   # pura file ka text le liya
        lines = content.split("\n")  # lines mei tod diya
        for line in lines:
            row = line.split(",")    # comma se tod diya
            data.append(row)         # list ke andar daal diya
    return data


if __name__ == "__main__":
    result = parse_csv("sample.csv")
    print(result)
