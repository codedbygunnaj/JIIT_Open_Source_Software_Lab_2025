def handlingFile(filePath, fileMode):
    with open(filePath, fileMode) as f:  
        # Reading
        readContent = f.read()   # pura file ek string ban jaega
        print("File Content:\n", readContent)

    with open(filePath, fileMode) as f:  
        readLines = f.readlines()   # sari lines ek list ban jaengi
        print("File Lines:\n", readLines)

    with open(filePath, "a") as f:  # append mode so old data na delete ho
        val = "For academic or formal papers, paragraphs might span more lines.\n"
        f.write(val)

        # writelines requires iterable of strings
        f.writelines([
            "A paragraph usually deals with a single idea.\n", 
            "In general, you'll have an introductory sentence expressing that idea.\n", 
            "And several supporting sentences to round it off.\n",
            "Paragraphs are usually about 100 to 200 words long.\n"
        ])


def handlingFile(filePath, fileMode):
    with open(filePath, fileMode) as f:  # mode is r+
        # Step 1: Read all content
        readContent = f.read()
        print("Full Content:\n", readContent)

        # Step 2: Seek back to start of file for reading line-by-line
        f.seek(0)  # moves cursor back to start
        readLine = f.readline()
        print("First Line:\n", readLine)

        # Step 3: Move cursor to end to append new content
        f.seek(0, 2)  # (0,2) → move to end of file
        val = "For academic or formal papers, paragraphs might span more lines.\n"
        f.write(val)

        # Step 4: Write multiple lines
        more_lines = [
            'A paragraph usually deals with a single idea.\n',
            'In general, you’ll have an introductory sentence expressing that idea.\n',
            'Several supporting sentences round it off.\n',
            'Paragraphs are usually about 100 to 200 words long.\n'
        ]
        f.writelines(more_lines)
