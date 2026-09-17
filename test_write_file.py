
#To import from a subdirectory, use this syntax: from DIRNAME.FILENAME import FUNCTION_NAME

#Where DIRNAME is the name of the subdirectory, FILENAME is the name of the file without 
#the .py extension, and FUNCTION_NAME is the name of the function you want to import.

from functions.write_file import write_file

print("Result for current file writes:")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
