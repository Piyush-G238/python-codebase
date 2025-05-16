# file handling in python
# working with files and directory in commonly done using below modules:
# os
# shutil
# pathlib
# open()

# directory operations

import os
import shutil

curr_dir = os.getcwd()
entries = os.listdir(curr_dir)
print(entries)

# os.mkdir("python_folder")
# os.mkdir("java_folder")
# os.rename("python_folder", "php_src")
# os.rmdir("php_src")

# with open("sample.txt", "w") as f:
#     f.write("""
#     Hi everybody,
#     My name is Piyush the developer and
#     please subscribe to my channel""")
#
# print("file writing done!")

with open("sample.txt", "a") as f:
    f.write("\nToday, I will explaining basics of system design")

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

shutil.copy("sample.txt", "samplecopy.text")