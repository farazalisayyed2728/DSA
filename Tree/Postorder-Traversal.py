def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data)