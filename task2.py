def doubleWriting(filename):
    f = open(filename, 'r')
    s = f.read()
    f = open(filename, 'a')
    f.write(s)
    f.close()

doubleWriting('CM1/file.txt')