______________________________________________________________________________
# Task 2: Write and Append Data to a File
'''
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''
______________________________________________________________________________

user_input = input("Enter text to write to the file :")
try :
    with open("output.txt","r+") as file:
        file.write(user_input + "\n")
        print("Data successfully written to output.txt\n")

    user_input = input("Enter addational text to append :")
    with open("output.txt","a") as file :
        file.write(user_input)
        print("Data successfully appended\n")

    print("Final content of output.txt")
    with open("output.txt","r+") as file :
        for x in file.readlines() :
            print(x.strip())
        file.close()
except FileNotFoundError :
    print("File not found")
