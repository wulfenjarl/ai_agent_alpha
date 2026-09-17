
#To import from a subdirectory, use this syntax: from DIRNAME.FILENAME import FUNCTION_NAME

#Where DIRNAME is the name of the subdirectory, FILENAME is the name of the file without 
#the .py extension, and FUNCTION_NAME is the name of the function you want to import.

from functions.get_files_info import get_files_info

print("Result for current directory:")
print(get_files_info("calculator", "."))
print("Result for pkg directory:")
print(get_files_info("calculator", "pkg"))
print("Result for /bin directory:")
print(get_files_info("calculator", "/bin"))
print("Result for ../ directory:")
print(get_files_info("calculator", "../"))

