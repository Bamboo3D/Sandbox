from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from panda3d.core import *
from editor import Editor
from navbar import NavBar

class MyApp(DirectObject):

    def __init__(self):
        # Create a window
        self.win = base.win
        self.win.setClearColor(Vec4(0.5, 0.5, 0.5, 1))

        # Initialize the editor
        self.editor = Editor(base)

        # Add event listeners
        self.accept("escape", self.quit)
        self.navbar = NavBar(self.editor) # Pass editor instance
        self.navbar.frame.reparentTo(base.a2dTopLeft)

    def quit(self):
        # Quit the application
        self.editor.destroy()
        base.userExit()

if __name__ == "__main__":
    # Create a new instance of ShowBase
    base = ShowBase()

    # Create a new instance of MyApp
    app = MyApp()

    # Run the game loop
    while True:
        base.taskMgr.step()
