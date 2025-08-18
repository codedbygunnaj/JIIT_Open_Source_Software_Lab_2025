# wrap.py

def wrap(fileLoc, mode, width):
    with open(fileLoc, mode) as f:
        content = f.read()

    # break content into chunks of given width
    wrapped_lines = []
    for i in range(0, len(content), width):
        wrapped_lines.append(content[i:i+width] + "\n")

    # overwrite file with wrapped lines
    with open(fileLoc, "w") as f:
        f.writelines(wrapped_lines)


# Run from here
if __name__ == "__main__":
    file_name = "/workspaces/JIIT_Open_Source_Software_Lab_2025/Week_2_2024/testFile.txt"
    wrap(file_name, "r", 20)   # wraps text into width of 20 characters
    print(f"File '{file_name}' has been wrapped to width 20.")
