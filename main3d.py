from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Mesh

class Object2d(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.drawObj()
    
    def drawObj(self):
        Mesh(vertices=[100,100,0,0, 200,200,0,0, 300,100,0,0],
             indices=[0,1,1,2,2,0],
             mode='lines')

class Game2d(App):
    def build(self):
        return Object2d()

Game2d().run()
