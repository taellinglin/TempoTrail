from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectButton import DirectButton

class TempoTrailGame(ShowBase):
    def __init__(self):
        super().__init__()

        # Set up a variable to store the current scene
        self.current_scene = None

        # Load the title screen
        self.load_title_screen()

    def load_title_screen(self):
        self.title_text = OnscreenText(
            text="Tempo Trail",
            pos=(0, 0),
            scale=0.1,
            fg=(1, 1, 1, 1),
            align=1,
            mayChange=True
        )

        self.start_button = DirectButton(
            text="Start Game",
            scale=0.1,
            pos=(0, 0, -0.2),
            command=self.load_game_scene
        )

    def load_game_scene(self):
        if self.current_scene:
            self.current_scene.removeNode()
        
        # Load a simple level, for demonstration, a colored plane
        self.current_scene = self.loader.loadModel("models/colored_plane.egg")
        self.current_scene.setPos(0, 0, 0)
        self.current_scene.reparentTo(self.render)

        # Load the player model with animation (replace with your actual player model)
        player = self.loader.loadModel("models/player.gltf")
        player.setPos(0, 0, 1)
        player.reparentTo(self.render)

app = TempoTrailGame()
app.run()
