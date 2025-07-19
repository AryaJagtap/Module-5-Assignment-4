______________________________________________________________________________
# Task 1: Read a File and Handle Errors  
'''
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''
______________________________________________________________________________

try :
    file = open("sample.txt", "r")
    printing_line = file.readlines()
    print("Reading the file content :")
    for x in printing_line:
        print(x.strip())
    file.close()
except FileNotFoundError :
    print("Error : The file Sample.txt was not found.")
finally:
    print("Continue with the program")
