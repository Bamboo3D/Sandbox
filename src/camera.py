from panda3d.core import Camera, PerspectiveLens

class Camera:

    def __init__(self, x=0, y=0, z=0):
        # Create a new camera node
        self.node = Camera("Camera")

        # Set the default camera properties
        self.node.set_lens(PerspectiveLens())
        self.node.set_pos(x, y, z)
        self.node.look_at(0, 0, 0)

    def set_pos(self, x, y, z):
        # Set the position of the camera node
        self.node.set_pos(x, y, z)

    def set_hpr(self, h, p, r):
        # Set the orientation of the camera node
        self.node.set_hpr(h, p, r)

    def set_lens(self, lens):
        # Set the lens of the camera node
        self.node.set_lens(lens)

    def get_node(self):
        # Get the camera node
        return self.node

    def destroy(self):
        # Destroy the camera node
        self.node.remove_node()
