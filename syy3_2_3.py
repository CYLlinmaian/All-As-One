fname = input("请输入要写入的文件: ")
fo = open(fname, "w+")
ls = ["小陈", "热爱", "生活"]
fo.writelines(ls)
for line in fo:
    print(line)
fo.close()