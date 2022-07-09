from math import sqrt
def getNum():       
    nums = []
    iNumStr = input("请输入数字(直接输入回车退出): ")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(直接输入回车退出): ")
    return nums

def mean(numbers):  #计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)

def dev(numbers, mean): #计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return sqrt(sdev / (len(numbers)-1))

def median(numbers):    #计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med
def max(numbers):     #计算最大值
    x = sorted(numbers)
    max=x[-1]
    return max
def min(numbers):  #计算最小值
    x = sorted(numbers)
    min=x[0]
    return min  
n =  getNum() #主体函数
m =  mean(n)
print("平均值:{},方差:{:.2},中位数:{}，最大值{},最小值{}".format(m, dev(n,m),median(n),max(n),min(n)))
