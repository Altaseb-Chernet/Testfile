with  open('example.txt') as f: #default mode is read
    line = f.read(10)
    print(line)

    lines = f.readline()
    print(lines)

    lines1 = f.readlines()
    for l in lines1:
        print(l.upper())
f.close()