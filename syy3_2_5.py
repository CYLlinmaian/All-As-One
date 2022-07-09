with open("1.txt","r") as f1,open("2.txt","w") as f2:
    for i in f1:
        i=i.replace(i,i.upper())
    f2.write(i)
