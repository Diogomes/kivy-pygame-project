from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class incrementador(BoxLayout):
    pass
class Test(App):
    def build(self):        
        return incrementador()

Test().run()
