
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image

Window.size = 360, 640

class TelaInicial(App):
    def __init__(self, **kwargs):
        Window.clearcolor = get_color_from_hex("#ffc1d5")
        super(TelaInicial, self).__init__(**kwargs)
        
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=[120, 120], spacing=10)
        
        layout.add_widget(Image(source='perfil-removebg-preview (1).png', size_hint=(None,None),size=(210,150)))

        layout.add_widget(Label(text='Seja Bem-Vindo(a)', font_size=40, font_name='Impact', color=get_color_from_hex('#FE70BD')))
        
        self.email_input = TextInput(hint_text="Email:")
        layout.add_widget(Label(text="Email:", font_name='Impact', color=get_color_from_hex('#FE70BD'), font_size=20))
        layout.add_widget(self.email_input)
        
        self.senha_input = TextInput(hint_text="Senha:", password=True)
        layout.add_widget(Label(text="Senha:", font_name='Impact', color=get_color_from_hex('#FE70BD'), font_size=20))
        layout.add_widget(self.senha_input)

        self.button_login = Button(text='Login', background_color=('#FE70BD'))
        layout.add_widget(self.button_login)
        
        self.button_cadastrar = Button(text='Cadastro', background_color=('#FE70BD'))
        layout.add_widget(self.button_cadastrar)
        
        return layout

if __name__ == '__main__':
    TelaInicial().run()
