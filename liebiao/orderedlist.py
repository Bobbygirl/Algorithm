from 算法.liebiao.Node import  Node

"""
顺序链表
size()判断元素个数：从头部开始遍历，计数
isEmpty()判断是否为空链表：只需要判断头部是否为空即可
remove(item)删除元素:首先要遍历查找该元素再使pre指向current.next
search(item）查找元素
add(item)在头部添加元素：temp.setNext(self.head) ,self.head=temp

"""
class orderedlist:
    #初始化
    def __init__(self):
        self.head=None

    #元素个数
    def size(self):
        current=self.head
        count=0
        while current.getNext()!=None:
            current=current.getNext()
            count+=1
        return count
    #判断是否为空
    def isEmpty(self):
        return self.head==None

    #删除元素
    def remove(self,item):
        current=self.head
        found=False
        pre=None
        while current!=None and not found:
            if current.getData()==item:
                 found=True
            else:
                pre=current
                current=current.getNext()
        if pre==None:
            self.head=current.getNext()
        else:
            pre.setNext(current.getNext())


    #查找某个元素
    def search(self,item):
        current=self.head
        found=False
        stop=False
        while current!=None and not found and not stop:
            if current.getData()==item:
                found=True
            else:
                if current.getData()>item:
                    stop=True
                else:
                    current=current.getNext()
        return found
    #添加元素
    def add(self,item):
        current=self.head
        pre=None
        temp=Node(item)
        while current!=None:
            if current.getData()<item:
                pre=current
                current=current.getNext()
            else:
                temp.setNext(current)
                pre.setNext(temp)
            if pre==None:
                temp.setNext(self.head)
                self.head=temp

