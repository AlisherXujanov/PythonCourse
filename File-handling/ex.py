# import sys
# import os

# FILENAME = sys.argv[1]
# text = sys.argv[2:]

# if os.path.exists(FILENAME):
#     with open(FILENAME, "w") as file:
#         file.write(" ".join(text))
#         print("If block")
#         print("The file exists")
#         file.close()
# else:
#     with open(FILENAME, "x") as file:
#         file.write(" ".join(text))
#         print("Else block")
#         print("The file exists")
#         file.close()

# with open(FILENAME, "r") as file:
#     print(file.read())
#     file.close()
# ===========================================================
# READ FILE
# When we open the file we have to always remember to close it
# If we don't close it then we can't open it again until we restart the program
# For reading the file we use 'r' mode
# Also, if the file is NOT FOUND then it returns an error

# 1. read()      => reads whole file (we also can specify how many characters to read)
# 2. readline    => reads only one line
# 3. readlines() => reads the file line by line (all lines)
# 4. loop through the file line by line

# FILENAME = "test.txt"
# with open(FILENAME, 'r+') as f:
#     f.write("\nThis is new line")
#     for line in f.readlines():
#         print(line)

# ex:
#   f = open("myfile.txt", "r")
#       print(f.read())

# ===========================================================
# UPDATE A FILE
# To update an existing file, we use "a" mode or "w" mode
# --- (w)  write mode replaces the content of the file
# --- (a)  append mode appends the content to the end of the file
# ex:
#   f = open("myfile.txt", "a")
#   f.write("Now the file has more content!")
#   ----------------------------
#   using keyword WITH
#   with open("myfile.txt", "a") as f:
#       f.write("Now the file has more content!")
# ===========================================================
# DELETE A FILE
# To delete a file, we use os.remove() function
# ex:
#   import os
#   os.remove("myfile.txt")

# ===========================================================
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "t" - Text - Default value. Text mode

# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "b" - Binary - Binary mode (e.g. images)

# Combinations of modes:
# "a+" - Read and Append - Opens a file for reading and appending, creates the file if it does not exist
# "w+" - Write and Read - Opens a file for writing and reading, creates the file if it does not exist
# "r+" - Read and Write - Opens a file for reading and writing, error if the file does not exist
# ===========================================================
# WORKING WITH DIRECTORIES and os
# import os
# os.mkdir("myfolder") # => creates a folder
# os.rmdir("myfolder") # => removes a folder
# os.rename("oldname", "newname") # => renames a folder
# os.getcwd() # => returns the current working directory
# os.path.exists("myfolder") # => checks if the folder exists
# os.path.isdir("myfolder") # => checks if the folder exists
# os.path.isfile("myfile.txt") # => checks if the file exists
# os.path.join("myfolder", "myfile.txt") # => joins the folder and the file



# ===========================================================
# HOMEWORK
# 1. https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/
# 2. https://www.w3resource.com/python-exercises/file/
