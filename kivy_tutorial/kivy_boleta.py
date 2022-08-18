
from cgitb import text
from tkinter import Button
from turtle import pos
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle

class OpcionBoleta(ButtonBehavior, GridLayout):
    
    def __init__(self, image_path, propietario, suplente, hipocoristico, **kwargs):
        super(OpcionBoleta, self).__init__(**kwargs)        
        self.cols = 2 
        self.propietario = propietario        
        self.size = (350, 150)
        with self.canvas:
            Color(0.2, 0.5, 0.5, 0.5)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            
        self.add_widget(Image(source=image_path, pos=(20, 25), size= (100,100)))
        self.add_widget(Label(text=hipocoristico, pos=(200, 100), size= (30,30)))
        self.add_widget(Label(text=propietario, pos=(200, 60), size= (30,30)))
        self.add_widget(Label(text=suplente, pos=(200, 80), size= (30,30)))
        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_press(self):
        print(self.propietario)
        return super().on_press()


class BoletaScreen(GridLayout):
    def __init__(self) -> None:
        super(BoletaScreen, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='Boleta'))
        self.add_widget(Label(text=''))
        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Juan', 'Pedro', 'Sombrero para todos'))
        self.add_widget(OpcionBoleta('images/stitch.png', 'Mario', 'Galicia', 'Otro Sombrero para todos'))
        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Juan', 'Pedro', 'Sombrero para todos'))
        self.add_widget(OpcionBoleta('images/stitch.png', 'Mario', 'Galicia', 'Sombrero para todos'))
        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Juan', 'Pedro', 'Sombrero para todos'))
        self.add_widget(OpcionBoleta('images/stitch.png', 'Mario', 'Galicia', 'Sombrero para todos'))
        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Juan', 'Pedro', 'Sombrero para todos'))
        self.add_widget(OpcionBoleta('images/stitch.png', 'Mario', 'Galicia', 'Sombrero para todos'))
        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Juan', 'Pedro', 'Sombrero para todos'))

class MyApp(App):
    def build(self):
        return BoletaScreen()

if __name__ == "__main__":
    MyApp().run()