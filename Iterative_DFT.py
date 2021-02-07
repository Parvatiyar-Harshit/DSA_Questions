class Node:
    def __init__(self,data):
        self.data = data
        self.firstChild = None
        self.sibling = None

def postOrderIterative(root):
    if root is None:
        return

    s1=[]
    s2=[]

    s1.append(root)


    while s1:

        node = s1.pop()
        s2.append(node)

        if node.firstChild:
            s1.append(node.firstChild)
        if node.sibling:
            s1.append(node.sibling)

    while s2:
        node=s2.pop()
        print (node.data)

def postOrderRecursive(root):
    if(root == None):
        print('')
    else:
        if(root.firstChild!=None):
            postOrderRecursive(root.firstChild)
        if(root.sibling!=None):
            postOrderRecursive(root.sibling)
        print(root.data) 

#making the tree
root = Node('A') 
root.firstChild = Node('B') 
root.firstChild.sibling = Node('C') 
root.firstChild.sibling.sibling = Node('Z') 
root.firstChild.sibling.sibling.sibling = Node('U')
comfort_root = Node('W')
cr = Node('D')
root.firstChild.sibling.sibling.sibling.firstChild = comfort_root
comfort_root.sibling = Node('Y')
comfort_root.sibling.sibling = Node('X')
comfort_root.sibling.sibling.firstChild = Node('V')
comfort_root.sibling.sibling.firstChild.firstChild = Node('M')
comfort_root.sibling.sibling.firstChild.firstChild.sibling = Node('N') 
root.firstChild.firstChild = cr
cr.firstChild = Node('E')
cr.firstChild.firstChild = Node('G')
cr.firstChild.sibling = Node('F')
cr.firstChild.sibling.sibling = Node('Q')
cr.firstChild.sibling.firstChild = Node('H')
cr.firstChild.sibling.firstChild.sibling = Node('I')
cr.firstChild.sibling.firstChild.sibling.firstChild = Node('J') 
#making the tree

postOrderIterative(root)

print('')

postOrderRecursive(root)

