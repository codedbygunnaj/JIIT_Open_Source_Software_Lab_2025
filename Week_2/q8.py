# f = open("test.txt", "r")

# print(f.read())       # read whole file
# print(f.read(5))      # read first 5 characters
# print(f.readline())   # read one line
# print(f.readlines())  # read all lines in a list

# 4. Using with (Best Practice ✅)
# Automatically closes file for you:
# with open("test.txt", "r") as f:
#     for line in f:
#         print(line.strip())


with open("/workspaces/JIIT_Open_Source_Software_Lab_2025/Week_2/testFile.txt",'r+') as f:
    #r+ is for read+write:
    readMe=f.read()
    print(readMe)
    f.write("Hi, I am currently pursuing my BTech from IIT.")
    readMe=f.read()
    print(readMe)

    print(f.tell())
    f.seek(0)
    print(f.tell())
    readMe=f.read()
    readmeWords=readMe.split(' ')
    print(readmeWords[::-1])
