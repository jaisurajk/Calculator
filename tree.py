# author: Jaisuraj Kaleeswaran
# date: March 6, 2023
# file: tree.py makes a binary tree class and an expression tree that is the child of the binary tree
# input: Input data inserted into the tree
# output: The value(s) of the expression(s) based on root value and the values of the children of root
from stack import Stack
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self,newNodeVal):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.leftChild = self.leftChild
            self.leftChild = t
    def getLeftChild(self):
        return self.leftChild
    def insertRight(self,newNodeVal):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.rightChild = self.rightChild
            self.rightChild = t
    def getRightChild(self):
        return self.rightChild
    def getRootVal(self):
        return self.key
    def setRootVal(self, Obj):
        self.key = Obj
    def __str__(self):
#return self.key as a string
        bint = f"{self.key}"
        bint += '('
        if self.leftChild != None:
            bint += str(self.leftChild)
        bint += ')('
        if self.rightChild != None:
            bint += str(self.rightChild)
        bint += ')'
        return bint
class ExpTree(BinaryTree): #A childclass to BinaryTree called ExpTree
    def make_tree(postfix):
        s = Stack() #Create a stack
        for ch in postfix: #For each character in the postfix expression
            if ch.replace('.', '').isdigit() or ch.isdigit(): #If the character is a float/number
                s.push(ExpTree(ch))
            else:
                expt = ExpTree(ch)
                expt.rightChild = s.pop()
                expt.leftChild = s.pop()
                s.push(expt)
        return s.pop()
    def inorder(tree):
        bint = ''
        if tree != None:
            if tree.leftChild != None:
                bint += '('
                bint += ExpTree.inorder(tree.getLeftChild())
            bint += str(tree.getRootVal())
            if tree.rightChild != None:
                bint += ExpTree.inorder(tree.getRightChild())
                bint += ')'
        return bint
    def preorder(tree):
        bint = ''
        if tree != None:
            bint += str(tree.getRootVal())
            bint += ExpTree.preorder(tree.getLeftChild())
            bint += ExpTree.preorder(tree.getRightChild())
        return bint
    def postorder(tree):
        bint = ''
        if tree != None:
            bint += ExpTree.postorder(tree.getLeftChild())
            bint += ExpTree.postorder(tree.getRightChild())
            bint += str(tree.getRootVal())
        return bint
    def evaluate(tree): #Evaluate the expression tree
        if tree != None: #If tree is not None, evaluate the arithmetic expression of left and right
            l_num = ExpTree.evaluate(tree.getLeftChild())
            r_num = ExpTree.evaluate(tree.getRightChild())
            if tree.getRootVal() == '^':
                return l_num ** r_num
            elif tree.getRootVal() == '*':
                return l_num * r_num
            elif tree.getRootVal() == '/':
                return l_num / r_num
            elif tree.getRootVal() == '+':
                return l_num + r_num
            elif tree.getRootVal() == '-':
                return l_num - r_num
            else:
#If the root value is a number return it as a float else return 0.0
                if tree.getRootVal() == None:
                    return 0.0
                return float(tree.getRootVal())
        return None #Return None if the tree is empty
    def __str__(self):
        return ExpTree.inorder(self)
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
# test a BinaryTree
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild() == None
    assert r.getRightChild() == None
    assert str(r) == 'a()()'
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'
# test an ExpTree
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    print(tree)
    assert str(tree) == '(5+(2*3))'
    print('inorder:', ExpTree.inorder(tree))
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    print('postorder:', ExpTree.postorder(tree))
    assert ExpTree.preorder(tree) == '+5*23'
    print('preorder:', ExpTree.preorder(tree))
    assert ExpTree.evaluate(tree) == 11.0
    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
    print("All tests passed")