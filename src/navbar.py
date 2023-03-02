from panda3d.core import *
from direct.gui.DirectGui import *

class NavBar:

    def __init__(self, editor):
        # Store a reference to the editor instance
        self.editor = editor

        # Create a frame to hold the navbar
        self.frame = DirectFrame(
            frameSize=(-1, 1, -0.1, 0),
            frameColor=(0.2, 0.2, 0.2, 1)
        )

        # Add buttons to the navbar
        self.create_button("New Scene", pos=(-0.9, 0, 0))
        self.create_button("Open Scene", pos=(-0.7, 0, 0))
        self.create_button("Save Scene", pos=(-0.5, 0, 0))
        self.create_button("Undo", pos=(-0.3, 0, 0))
        self.create_button("Redo", pos=(-0.1, 0, 0))

    def create_button(self, label, **kwargs):
        # Create a button with the given label and options
        button = DirectButton(
            parent=self.frame,
            text=label,
            text_scale=0.05,
            text_align=TextNode.ACenter,
            text_fg=(1, 1, 1, 1),
            text_shadow=(0, 0, 0, 1),
            frameSize=(-0.2, 0.2, -0.05, 0.05),
            frameColor=(0.3, 0.3, 0.3, 1),
            relief=DGG.FLAT,
            **kwargs
        )

        return button

    def destroy(self):
        # Destroy the navbar
        self.frame.destroy()

    def update(self):
        # Update the navbar
        pass
