# get a directory's size by iterate through all files and directories in it
import os

total_size = 0
for folderName, subFolders, filenames in os.walk('.'):
    dir_total_size = total_size + os.path.getsize(filenames)
    print(folderName + ':' + str(dir_total_size))
    total_size += dir_total_size

print(total_size)
