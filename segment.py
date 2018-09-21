import jieba
'''
get segment result
'''

def getSegment(line):
    linelist = jieba.cut(line)
    arrayList = []
    for word in linelist:
        arrayList.append(word)
    #print(arrayList)
    return arrayList


if __name__=="__main__":
    list = getSegment("南京市长江大桥")
    for i in range(len(list)):
        print(list[i])



