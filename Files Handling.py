# 'a' append >> open file for appending values, creat file if not exists
# 'r' read [default] open file for read & give error if file not exists
# 'w' write open file for writing, creat file if not exists
# 'x' create file , give error error if file not exists
# ---------------------------------------------------------

# “absolute path” from rote of your pc to the current place
# as 'E:\python traning\files\Ahmed.txt' and directly

# 'relative path' from current path >> as 'files\Ahmed.txt'
# it work by         >>  os.getcwd()
# then relative path >> 'files\Ahmed.txt'
# import os
# # main current working directory
# print(os.getcwd())

# print(os.path.abspath(__file__))
# print('#'*60)

# # Directory for opened file

# print(os.path.dirname(os.path.abspath(__file__)))

# # change current workig directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# r >> raw string (r'')
# myFile = open(r"E:\python trainning\files\bolbol.txt", 'r' )
# print(myFile.name) # file data object
# print(myFile.mode)
# print(myFile.encoding)
# print(myFile)

# Reading file
# print(myFile.read())
print('#'*60)

# print(myFile.readline(20))

# print(myFile.readlines())

# for line in myFile:
#     print(line)
#     if line.startswith('where'):
#         break

# myFile.close()
print('#'*60)

# write & append
# f2 = open(r"E:\python trainning\files\Ahmed.txt", 'w')
# f2.write('Hi Ahmed form python , how are you?\n')
# f2.write('Good luck in your job.')

# f2.writelines(['hi omar\n' , 'hi abdo\n', 'hi hazem\n'])

# f2 = open(r"E:\python trainning\files\Ahmed.txt", 'a')
# f2.write('Hi mostafa , what\'s your skill?\n')
# l = ['cairo\n', 'alex\n']
# f2.writelines(l)
# f2.truncate(10)
# print(f2.tell())

# f2 = open(r"E:\python trainning\files\Ahmed.txt", 'r')
# f2.seek(3)
# print(f2.read())

# import os
# os.getcwd()

# os.remove(r'files\Ahmed.txt')