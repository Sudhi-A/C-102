import os
import shutil
'''
print(dir(os))

os.getcwd()
os.mkdir("New")
os.listdir()
os.path.exists("New")
'''

path = 'New'

isExist = os.path.exists(path)
print(isExist)

print("Before copying all files:")
print(os.listdir(path))
source = "feather.jfif"
destination = "New/copyfeather.jfif"

dest = shutil.copy(source,destination)
print("After copying files")
print(os.listdir(path))