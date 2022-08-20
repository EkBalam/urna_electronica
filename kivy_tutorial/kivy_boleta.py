
from cgitb import text
from tkinter import Button, font
from turtle import pos
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.core.window import Window



class OpcionBoleta(ButtonBehavior, BoxLayout):
    
    def __init__(self, image_path, propietario, suplente, hipocoristico, color = (0.2, 0.5, 0.5, 0.5), **kwargs):
        super(OpcionBoleta, self).__init__(**kwargs)        
        self.padding = [50, 50]
        self.cols = 2 
        self.propietario = propietario        
        self.size = (500, 150)
        self.rect_size = (self.size[0]-10, self.size[1]-10)
        
        with self.canvas:            
            Color(rgba = color)       
            self.rect = RoundedRectangle(pos=self.pos, size=self.rect_size, radius = [(20, 20), (20, 20)])
            
        self.add_widget(Image(source=image_path, pos=(20, 25), size= (100,100), pos_hint = {"x": 0.01, "y": 0.01}, size_hint =(0.4, 1)))
        
        gl = GridLayout(cols=1)
        gl.add_widget(Label(text=hipocoristico, font_size = 32))
        gl.add_widget(Label(text='Propietario', font_size = 16, size_hint =(.99, .99)))
        gl.add_widget(Label(text=propietario, font_size = 32))
        gl.add_widget(Label(text='Suplente', font_size = 16, size_hint =(.99, .99)))
        gl.add_widget(Label(text=suplente, font_size = 32))

        self.add_widget(gl)

        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect_size = (self.size[0]-10, self.size[1]-10)
        self.rect.size = self.rect_size

    def on_press(self):
        print(self.propietario)
        return super().on_press()


class BoletaScreen(GridLayout):
    def __init__(self, **kwargs) -> None:
        super(BoletaScreen, self).__init__(**kwargs)        
        self.cols = 4        
        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Propietario', 'Suplente', 'Partido Sombrero', color=(0.52549, 0.07451, 0.07451, 1)))
        self.add_widget(OpcionBoleta('images/img2.png', 'Mario', 'Galicia', 'Partido Paraiso', color=(0.07451, 0.52549, 0.18824, 1)))
        self.add_widget(OpcionBoleta('images/img2.png', 'Miguel', 'Blue', 'Partido Paraiso', color=(0.07451, 0.52549, 0.18824, 1)))
        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Juan', 'Pedro', 'Partido Sombrero', color=(0.52549, 0.07451, 0.07451, 1)))

        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Propietario', 'Suplente', 'Partido Sombrero', color=(0.52549, 0.07451, 0.07451, 1)))
        self.add_widget(OpcionBoleta('images/img2.png', 'Mario', 'Galicia', 'Partido Paraiso', color=(0.07451, 0.52549, 0.18824, 1)))
        self.add_widget(OpcionBoleta('images/img2.png', 'Miguel', 'Blue', 'Partido Paraiso', color=(0.07451, 0.52549, 0.18824, 1)))
        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Juan', 'Pedro', 'Partido Sombrero', color=(0.52549, 0.07451, 0.07451, 1)))

        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Propietario', 'Suplente', 'Partido Sombrero', color=(0.52549, 0.07451, 0.07451, 1)))
        self.add_widget(OpcionBoleta('images/img2.png', 'Mario', 'Galicia', 'Partido Paraiso', color=(0.07451, 0.52549, 0.18824, 1)))
        self.add_widget(OpcionBoleta('images/img2.png', 'Miguel', 'Blue', 'Partido Paraiso', color=(0.07451, 0.52549, 0.18824, 1)))
        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Juan', 'Pedro', 'Partido Sombrero', color=(0.52549, 0.07451, 0.07451, 1)))


class MyApp(App):
    def build(self):
        bs = BoletaScreen(pos_hint = {"x": 0.01, "y": 0.01}, size_hint =(.99, .99), padding = (10, 10))
        bl = BoxLayout(orientation='vertical')
        bl.add_widget(Label(text='Boleta para Votar', font_size=32, color = [0,0,0,1], size_hint = (1, .1)))
        bl.add_widget(bs)
        return bl

if __name__ == "__main__":
    Window.size = (1920, 1080)
    Window.clearcolor = (0.96863, 0.85490, 0.72941, 1)
    MyApp().run()