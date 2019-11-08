"""
二叉堆的实现
根的值要小于或等于左右孩子的值
"""
from pythonds.trees.binheap import  BinHeap
class BinHeap:
    def __init__(self):
        #初始化列表
        self.heapList = [0]
        #记录堆大小
        self.currentSize = 0
    def BuildHeap(self,alist):
        """
        创建二叉堆(需要排序)
        """
        #使用二分法搜索，
        i=len(alist)//2
        #获取列表长度
        self.currentSize=len(alist)
        #获取定义列表
        self.heapList =[0]+alist[:]
        #要实现有序，需要将大项下沉（方法，跟自己左右孩子比较大小，调用perDown函数）
        while(i>0):
            self.percDown(i)
            i=i-1

    def percUp(self,i):
        """

        上浮，插入一个数据项，如果较小就上浮
        """
        #i//2是获得根的值
        while i//2>0:
            #比较当前值和根值的大小，如果孩子节点的值小，则交换位置
            if self.heapList[i]<self.heapList[i//2]:
                self.heapList[i],self.heapList[i//2]=self.heapList[i//2],self.heapList[i]
        i=i//2

    def insert(self,k):
        """
            二叉堆的插入算法
        """
        #首先将节点加入到列表中
        self.heapList.append(k)
        #列表长度+1
        self.currentSize +=1
        #调用percUp()上浮
        self.percUp(self.currentSize)

    def percDown(self,i):
        """
           数字下沉
        """
        #首先判断节点的位置i*2是否在列表中：
        while(i*2)<=self.currentSize:
            #如果在获取左右孩子的最小项，调用minChild()
            mc=self.minChild(i)
            #判断当前数据项和mc的大小关系，然后交换位置
            if self.heapList[i]>self.heapList[mc]:
                self.heapList[i],self.heapList[mc]=self.heapList[mc],self.heapList[i]
            i=mc


    def minChild(self,i):
        """
            交换节点
        """
        #首先判断i*2+1是否在超出列表长度
        if i*2+1>self.currentSize:
            return i*2
        else:
            #若没有超出，则比较左右孩子的数据项的大小
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        """
            删除最小的数据项
        """
        #获取最小项，即根节点
        reval=self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize -=1
        # self.heapList.pop()
        self.percDown(1)
        return reval
if __name__=='__main__':

    alist=BinHeap()
    alist.BuildHeap([5,9,11,14,18,19,21,33,17,27])
    print(alist.delMin())