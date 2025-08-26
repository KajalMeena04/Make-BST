# app.py
from flask import Flask, render_template, request
from bst import (
    Node, insert, delete, search, inorder, preorder, postorder, level_order,
    visualize_bst, getSuccessor, getPredecessor, minValue, maxValue, floor, ceil,
    height, count_nodes, count_leaves, path_to_node
)

app = Flask(__name__)
root = None  # Global BST root
image_file = None

@app.route("/", methods=["GET", "POST"])
def index():
    global root, image_file
    message = ""
    traversal = ""
    
    if request.method == "POST":
        action = request.form.get("action")
        value = request.form.get("value")
        if value:
            value = int(value)
        
        if action == "Insert":
            root = insert(root, value)
            message = f"{value} inserted."
        elif action == "Delete":
            root = delete(root, value)
            message = f"{value} deleted (if it existed)."
        elif action == "Search":
            node = search(root, value)
            message = f"{value} {'found' if node else 'not found'}."
        elif action == "Inorder":
            traversal = []
            def collect(node):
                if node:
                    collect(node.left)
                    traversal.append(str(node.key))
                    collect(node.right)
            collect(root)
            traversal = " -> ".join(traversal)
        elif action == "Preorder":
            traversal = []
            def collect(node):
                if node:
                    traversal.append(str(node.key))
                    collect(node.left)
                    collect(node.right)
            collect(root)
            traversal = " -> ".join(traversal)
        elif action == "Postorder":
            traversal = []
            def collect(node):
                if node:
                    collect(node.left)
                    collect(node.right)
                    traversal.append(str(node.key))
            collect(root)
            traversal = " -> ".join(traversal)
        elif action == "LevelOrder":
            traversal_list = []
            from collections import deque
            q = deque([root]) if root else deque()
            while q:
                node = q.popleft()
                traversal_list.append(str(node.key))
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            traversal = " -> ".join(traversal_list)
        elif action == "MinMax":
            traversal = f"Min: {minValue(root)}, Max: {maxValue(root)}"
        elif action == "FloorCeil":
            traversal = f"Floor: {floor(root, value)}, Ceil: {ceil(root, value)}"
        elif action == "SuccessorPredecessor":
            succ = getSuccessor(root, value)
            pred = getPredecessor(root, value)
            traversal = f"Successor: {succ.key if succ else None}, Predecessor: {pred.key if pred else None}"
        elif action == "Stats":
            traversal = f"Height: {height(root)}, Nodes: {count_nodes(root)}, Leaves: {count_leaves(root)}"
        elif action == "Path":
            path = path_to_node(root, value)
            traversal = " -> ".join(map(str, path)) if path else f"{value} not found"
    
    # Update the tree image
    image_file = visualize_bst(root, filename="static/bst") if root else None
    
    return render_template("index.html", message=message, traversal=traversal, image_file=image_file)

if __name__ == "__main__":
    app.run(debug=True)
