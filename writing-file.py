import os
# with open('example.txt','w') as file:
#     text = file.write('hello world')
#     print(text)

# file = open('example.txt','w')
# x = [1,4,5,6,7,8,9]
# file.write(','.join(map(str,(x))))#TypeError: write() argument must be str, not list
# file.close()


# with open('example.txt') as file:
#     content = file.readlines()
#     print(list(content))

# file = open('example.txt','a')
# file.write('\nhello world, ')
# file.write('\nhello Africa, ')
# file.write('\nhello Ethiopa, ')
# file.close()

# with open('example.txt','r') as file:
    # content = file.read()
    # print(content)

    # lines = file.readlines()
    # print(lines)

from datetime import datetime
now = datetime.now()
print(now)