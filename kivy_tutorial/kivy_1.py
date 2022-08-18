import kivy
kivy.require('2.1.0')

from kivy.app import App

#uix = user interface X
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

class LoginScreen(GridLayout):

    def __init__(self, **kwargs) -> None:
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Nombre de usuario'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Contraseña'))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)
        self.add_widget(Button(text='Presioname mucho...'))
        self.add_widget(Image(source='images/sombrerito.webp'))


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__=='__main__':
    MyApp().run()