import os
import shutil
print(dir(os))
print(os.listdir())
print(os.getcwd())
path = 'C:/Users/Lakshmi Ganesh/Downloads/C-102/Sudhanshu/Text.txt'
isExist = os.path.exists(path)
print(isExist)
True
path = 'C:/Users/Lakshmi Ganesh/Downloads/C-102/Sudhanshu/Text.txt'
isExist = os.path.exists(path)
print(isExist)
False

#os.path.exists("C:/Users/Lakshmi Ganesh/Downloads/C-102/Sudhanshu/Text.txt")

source = 'C:\\Users\\Lakshmi Ganesh\\Downloads\\C-102\\Sudhanshu\\Text.txt'
destination = 'C:\\Users\\Lakshmi Ganesh\\Downloads\\C-102\\Sudhanshu\\Textcopy.txt'
dest = shutil.copy(source,destination)
print("After Copying File")
print(os.listdir(path))