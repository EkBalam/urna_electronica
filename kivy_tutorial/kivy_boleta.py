
from cgitb import text
from turtle import color
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

class EncabezadoBoleta(BoxLayout):
    def __init__(self, image_path, eleccion, entidad, distrito, municipio, color = (1, 1, 1, 1), **kwargs):
        super(EncabezadoBoleta, self).__init__(**kwargs)
        ople_color = (0.90196, 0.00000, 0.45098, 1)
        text_color = (0, 0, 0, 1)

        self.size_hint = (1, .2)
        self.rect_size = self.size
        self.rect_size2 = (self.rect_size[0]-10,self.rect_size[1]-10)
        with self.canvas:            
            Color(rgba = ople_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.rect_size , radius = [(0, 0), (0, 0), (20, 20), (20, 20)])
            
            Color(rgba = color)
            self.rect2 = RoundedRectangle(pos=(self.pos[0]+5, self.pos[1]+5), size=self.rect_size2, radius = [(0, 0), (0, 0), (20, 20), (20, 20)])
            
                
        self.add_widget(Image(source=image_path, pos_hint = {"x": 0.2, "y": 0.1}, size_hint =(0.4, 0.8)))
        
        bl = BoxLayout(orientation='vertical')        
        bl.add_widget(Label(text=eleccion, font_size = 56, color = ople_color))
        bl.add_widget(Label(text=f'Entidad Federativa: {entidad}     Distrito electoral local: {distrito}    Municipio: {municipio}', 
                            pos_hint ={"x": 0.01, "y": 0.1}, font_size = 32, color = text_color, halign="left", valign="middle"))        
        bl.add_widget(Label(text='Presione en el recuadro de su preferencia', font_size = 32, color = ople_color, size_hint =(.99, .99), halign="left", valign="middle"))

        self.add_widget(bl)

        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect_size = self.size
        self.rect.size = self.rect_size
        
        self.rect2.pos = (self.pos[0]+5, self.pos[1]+5)
        self.rect_size2 = (self.rect_size[0]-10,self.rect_size[1]-10) 
        self.rect2.size = self.rect_size2


class OpcionBoleta(ButtonBehavior, BoxLayout):
    
    def __init__(self, image_path, propietario, suplente, hipocoristico, color = (0.2, 0.5, 0.5, 0.5), text_color = (1, 1, 1, 1), **kwargs):
        super(OpcionBoleta, self).__init__(**kwargs)        
        self.padding = [50, 50]
        #self.cols = 2 
        self.propietario = propietario        
        self.hipocoristico = hipocoristico
        self.img_path = image_path
        self.size = (500, 150)
        self.rect_size = (self.size[0]-10, self.size[1]-10)
        
        with self.canvas:            
            Color(rgba = color)       
            self.rect = RoundedRectangle(pos=self.pos, size=self.rect_size, radius = [(20, 20), (20, 20)])
            
        self.add_widget(Image(source=image_path, pos_hint = {"x": 0.01, "y": 0.01}, size_hint =(0.4, 1)))
        
        ople_color = (0.90196, 0.00000, 0.45098, 1)
        gl = GridLayout(cols=1)
        gl.add_widget(Label(text=hipocoristico, font_size = 32, color = ople_color))
        gl.add_widget(Label(text='Propietario', font_size = 16, color = text_color, size_hint =(.99, .99)))
        gl.add_widget(Label(text=propietario, font_size = 32, color = ople_color))
        gl.add_widget(Label(text='Suplente', font_size = 16, color = text_color, size_hint =(.99, .99)))
        gl.add_widget(Label(text=suplente, font_size = 32, color = ople_color))

        self.add_widget(gl)

        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect_size = (self.size[0]-10, self.size[1]-10)
        self.rect.size = self.rect_size

    def on_press(self):
        view = AceptarVoto(self.propietario, self.hipocoristico, self.img_path)
        view.open()
        print(self.propietario)
        return super().on_press()


class BoletaScreen(GridLayout):
    def __init__(self, **kwargs) -> None:
        super(BoletaScreen, self).__init__(**kwargs)        
        self.cols = 3     

        blanco = (1.00000, 1.00000, 1.00000, 1)
        rojo = (0.60000, 0.00000, 0.00000, 1)
        amarillo = (1.00000, 1.00000, 0.00000, 1)
        azul = (0.00000, 0.00000, 0.80000, 1)
        negro = (0, 0, 0, 1)

        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Natalia Jarquin Morales', 
        'Zain Aziel Morales Martínez', 'Partido Sombrero', color=rojo))

        self.add_widget(OpcionBoleta('images/img2.png', 'Norma Ines Jiménez Ponce', 
        'Brenda Reyes Vázquez', 'Partido Paraiso', color=blanco, text_color=negro))

        self.add_widget(OpcionBoleta('images/img2.png', 'Miguel Ávarez Castillo', 
        'Zain Aziel Morales Martínez', 'Partido Paraiso', color=azul))

        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Juan Jimenez', 
        'Pedro García', 'Partido Sombrero', color=amarillo, text_color=negro))   

        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Natalia Jarquin Morales', 
        'Zain Aziel Morales Martínez', 'Partido Sombrero', color=rojo))

        self.add_widget(OpcionBoleta('images/img2.png', 'Norma Ines Jiménez Ponce', 
        'Brenda Reyes Vázquez', 'Partido Paraiso', color=blanco, text_color=negro))

        self.add_widget(OpcionBoleta('images/img2.png', 'Miguel Ávarez Castillo', 
        'Zain Aziel Morales Martínez', 'Partido Paraiso', color=azul))

        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Juan Jimenez', 
        'Pedro García', 'Partido Sombrero', color=amarillo, text_color=negro))   

        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Natalia Jarquin Morales', 
        'Zain Aziel Morales Martínez', 'Partido Sombrero', color=rojo))

        self.add_widget(OpcionBoleta('images/img2.png', 'Norma Ines Jiménez Ponce', 
        'Brenda Reyes Vázquez', 'Partido Paraiso', color=blanco, text_color=negro))

        self.add_widget(OpcionBoleta('images/img2.png', 'Miguel Ávarez Castillo', 
        'Zain Aziel Morales Martínez', 'Partido Paraiso', color=azul))

        self.add_widget(OpcionBoleta('images/sombrerito.webp', 'Juan Jimenez', 
        'Pedro García', 'Partido Sombrero', color=amarillo, text_color=negro))        


class AceptarVoto(ModalView):

    def __init__(self, propietario, partido, img_path,  **kwargs):
        super(AceptarVoto, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (600, 600)
        self.auto_dismiss = False
        
        with self.canvas:            
            Color(rgba = (1.00000, 0.90196, 0.80000, 1))       
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius = [(20, 20), (20, 20)])

        ople_color = (0.90196, 0.00000, 0.45098, 1)

        boxL = BoxLayout(orientation='vertical', padding=(20))
        boxL.add_widget(Label(text='Está es su elección de voto\n presione ACEPTAR para registrarlo\n o CANCELAR para regresar', 
                                font_size = 32, color = (0,0,0,1)))
        
        boxL.add_widget(Label(text=propietario, font_size = 36, color = ople_color))
        self.add_widget(Image(source=img_path, size_hint =(0.2, 0.5)))                     
        boxL.add_widget(Label(text=partido, font_size = 36, color = ople_color))


        gl = GridLayout(cols=2, padding=(24))
        self.button_aceptar = Button(text='ACEPTAR')
        gl.add_widget(self.button_aceptar)

        self.button_cancel = Button(text='CANCELAR')
        gl.add_widget(self.button_cancel)
        
        boxL.add_widget(gl)
        self.add_widget(boxL)        

        self.button_cancel.bind(on_press = self.dismiss)

        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class MyApp(App):
    def build(self):
        bs = BoletaScreen(pos_hint = {"x": 0.01, "y": 0.01}, size_hint =(.99, .99))
        enc = EncabezadoBoleta('images/opleVeracruz.png', 'Diputaciones Locales', 'Veracruz', '10', 'Xalapa')
        bl = BoxLayout(orientation='vertical')        
        bl.add_widget(enc)
        bl.add_widget(bs)
        return bl

if __name__ == "__main__":
    Window.size = (1920, 1080)
    Window.clearcolor = (1.00000, 0.90196, 0.80000, 1)
    MyApp().run()