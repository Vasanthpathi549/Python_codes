with open("file.txt",'r')as f:
    c=list(f.read())
    f.seek(0)
    w=f.read().split(" ")
    f.seek(0)
    l=list(f.readlines())
    print("No. of characters are",len(c))
    print("No. of words are",len(w))
    print("No. of lines are ",len(l))
