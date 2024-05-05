import io
import os

fileName = input("Enter name of file: ")
if os.path.exists(fileName):
    myFile = open(fileName, 'rt')
    while True:
        line = myFile.readline()
        if line != "":
            print(line, end ='')
        else:
            myFile.close()
            break