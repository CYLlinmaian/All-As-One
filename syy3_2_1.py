textFile = open("lin.txt","rt") #t 表示文本文件方式
print(textFile.readline())
textFile.close()
binFile = open("xiaolin.txt","rb") #r 表示二进制文件方式
print(binFile.readline())
binFile.close()
