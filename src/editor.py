from direct.gui.DirectGui import *
from panda3d.core import *
from scene import Scene
from navbar import NavBar

class Editor:

    def __init__(self, base):
        from camera import Camera # Import Camera here to avoid circular import

        # Store a reference to the ShowBase instance
        self.base = base

        # Create a scene graph and add a root node
        self.scene = Scene()
        self.root = self.scene.root_node

        # Create a camera and set its position
        self.camera = Camera()
        self.camera.set_pos(0, 0, 10)

        # Create a node to represent the camera in the scene graph
        self.camera_node = self.scene.create_node("Camera")
        self.camera_node.set_camera(self.camera)

        # Add the camera node to the root node
        self.root.add_child(self.camera_node)

        # Create a navbar and add it to the scene
        self.navbar = NavBar()
        self.navbar.frame.reparentTo(self.base.aspect2d)

    def destroy(self):
        # Destroy the editor
        self.navbar.destroy()
        self.camera.destroy()
        self.scene.destroy()

    def update(self):
        # Update the editor
        self.camera.update()
        self.scene.update()
        self.navbar.update()
