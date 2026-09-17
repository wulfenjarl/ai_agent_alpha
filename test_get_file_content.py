
#To import from a subdirectory, use this syntax: from DIRNAME.FILENAME import FUNCTION_NAME

#Where DIRNAME is the name of the subdirectory, FILENAME is the name of the file without 
#the .py extension, and FUNCTION_NAME is the name of the function you want to import.

from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")


#Once the lorem ipsum test is passing, add the following test cases and print their outputs. Print the smaller file/error cases, not the full lorem.txt contents:

print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))
