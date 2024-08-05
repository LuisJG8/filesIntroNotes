# myFile = open(file="nFile.txt", mode='w')
# myFileWrite = myFile.write("This is a file!!!\n")
#
# myFile.close()
#
# myFile = open(file="nFile.txt", mode='r')
# content = myFile.read()
# print(content)
# myFile.close()


with open("nFile.txt", mode="w") as writeFile:
    print("Writing...\n")
    theContent = writeFile.write("This is a new text\n\n")

with open("nFile.txt", mode="r") as readTfile:
    print("Reading...")
    readContent = readTfile.read()
    print(readContent)