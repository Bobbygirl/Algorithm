"""
冒泡排序
"""
def BubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
    return alist



if __name__=='__main__':
    print(BubbleSort([54,26,32,49,38,29]))
