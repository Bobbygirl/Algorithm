
"""
解析树
使用栈来追踪父节点和当前节点
"""
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
from pythonds.trees import BinarySearchTree
import operator
def buildparseTree(fpexp):
    #对字符串解析
    fplist=fpexp.split()
    #创建栈
    pstack=Stack()
    #创建树
    eTree=BinaryTree('')
    #栈的push()方法将树添加到栈中
    pstack.push(eTree)
    #使用current指向当前节点
    currentTree=eTree
    #对字符串进行遍历
    for i in fplist:
        if i=='(':
            #如果字符串为(,则在当前节点插入左孩子
            currentTree.insertLeft('')
            #添加到栈中
            pstack.push(currentTree)
            #当前节点指向左孩子节点
            currentTree=currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')']:
            #如果为数字,则在当前节点中添加
            currentTree.setRootVal(int(i))
            #出栈
            parent=pstack.pop()
            #将当前节点指向它的父节点
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
    """

    算值

    """
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftc=parsetree.getLeftChild()
    rightc=parsetree.getRightChild()
    if leftc and rightc:
        fn=opers[parsetree.getRootVal()]
        return fn(evalue(leftc),evalue(rightc))
    else:
        return parsetree.getRootVal()

def postorsereval(tree):
    """
    采用后序遍历法重写表达式求值代码
    """
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    res1=None
    res2=None
    if tree:
        res1=postorsereval(tree.getLeftChild())
        res2=postorsereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()
def preorder(tree):
    """
    前序遍历
    """
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
if __name__=='__main__':
    pt=buildparseTree("( ( 10 + 5 ) * 3 )")
    print(pt.postorder())
    print(postorsereval(pt))
    print(pt.inorder())