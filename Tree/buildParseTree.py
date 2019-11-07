
"""
解析树
"""
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator
def buildparseTree(fpexp):
    fplist=fpexp.split()
    #创建栈
    pstack=Stack()
    eTree=BinaryTree('')
    pstack.push(eTree)
    currentTree=eTree
    for i in fplist:
        if i=='(':
            currentTree.insertLeft('')
            pstack.push(currentTree)
            currentTree=currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')']:
            currentTree.setRootVal(int(i))
            parent=pstack.pop()
            currentTree=parent
        elif i in ['+','-','*','/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pstack.push(currentTree )
            currentTree =currentTree.getRightChild()
        elif i ==')':
            currentTree =pstack.pop()
        else:
            raise ValueError
    return currentTree
def evalue(parsetree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftc=parsetree.getLeftChild()
    rightc=parsetree.getRightChild()
    if leftc and rightc:
        fn=opers[parsetree.getRootVal()]
        return fn(evalue(leftc),evalue(rightc))
    else:
        return parsetree.getRootVal()
if __name__=='__main__':
    pt=buildparseTree("( ( 10 + 5 ) * 3 )")
    print(pt.postorder())
    print(evalue(pt))