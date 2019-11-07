from 算法.liebiao.Node import Node
"""
无序链表
add(item):在头部添加元素
size(item):计算元素个数
search(item):current=current.getNext()
append(item):在链表末尾添加元素current.setNext(temp)
remove(item)
insert(pos,item):perious.setNext(temp),temp.setNext(current)
"""
class unorderlist:

    def __init__(self):
        self.head=None
    #在链表前端添加元素
    def add(self,item):
        temp=Node(item)#创建临时变量指向当前要添加的节点
        temp.setNext(self.head)
        self.head=temp
    #元素个数
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    #查找指定元素是否存在,返回的是布尔类型true or false
    def search(self,item):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
        return found
    #删除指定元素（先查找再删除）
    def remove(self,item):
        current=self.head
        found=False
        perious=None
        while not found:
            if current.getData()==item:
                found=True
            else:
                perious=current
                current=current.getNext()
        if perious==None:
            self.head=current.getNext()
        else:
            perious.setNext(current.getNext())
    #在链表末尾追加元素O(n)
    def append(self,item):
        temp=Node(item)
        current=self.head
        if current is None:
            current=temp
        while current.getNext()!=None:
             current=current.getNext()
        current.setNext(temp)


    #指定位置插入元素,先找位置
    def insert(self,pos,item):
        current=self.head
        temp=Node(item)
        cur=0
        perious=None
        while cur < pos-1:

            perious=current
            current=current.getNext()
            cur=cur+1
        perious.setNext(temp)
        temp.setNext(current)



    #返回指定元素的位置
    def index(self,item):
        current=self.head
        cur=0
        while current!=None:
            if current.getData()==item:
                return cur
            else:

                current=current.getNext()
                cur+=1

    def pop(self):
        pass

if  __name__=='__main__':
    mylist=unorderlist()
    mylist.add(3)
    mylist.add(4)
    mylist.add(5)
    mylist.add(6)
    mylist.append(7)
    mylist.insert(3,9)
    # print(mylist.search(3))
    # mylist.remove(7)
    print(mylist.size())
    print(mylist.index(9))
