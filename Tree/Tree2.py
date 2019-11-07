"""
树的创建
使用节点实现树
"""
class BianryTree:
    def __init__(self,rootInt):
        self.key=rootInt
        self.leftChild=None
        self.rightChild=None
    def insertLeft(self,newnode):
        if self.leftChild ==None:
            self.leftChild=BianryTree(newnode)
        else:
            t=BianryTree(newnode)
            t.leftChild=self.leftChild
            self.leftChild=t
    def insertRight(self,newnode):
        if self.rightChild ==None:
            self.rightChild=BianryTree(newnode)
        else:
            t=BianryTree(newnode)
            t.rightChild=self.rightChild
            self.rightChild=t
    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def getRootVal(self):
        return self.key
    def setRootVal(self,Int):
        self.key=Int


if __name__=='__main__':
    r=BianryTree(5)
    # print(r.getRootVal())
    # print(r.getLeftChild())
    # print(r.getRightChild())
    r.insertLeft(2)
    print(r.getLeftChild().getRootVal())
    r.insertLeft(4)
    print(r.getLeftChild().getRootVal())
    r.insertRight(3)
    print(r.getRightChild().getRootVal())