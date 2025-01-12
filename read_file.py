import os
print(os.getcwd())

#reading
#read()

file = open('example.txt','r')
# content = file.read()
# print(content)
# file.close()

#readline

# line = file.readline()
# while line:
#     print(line,end='')
#     line = file.readline()

#readlines
lines = file.readlines()
for i in lines:
    print(i,end='')