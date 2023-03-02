from panda3d.core import *

class Scene:

    def __init__(self):
        # Create a NodePath for the root node
        self.root_node = NodePath("Root")

    def create_node(self, name):
        # Create a new NodePath with the given name
        node = NodePath(name)

        # Attach the node to the root node
        node.reparentTo(self.root_node)

        return node

    def destroy(self):
        # Destroy the scene graph
        self.root_node.removeNode()

    def update(self):
        # Update the scene graph
        pass
