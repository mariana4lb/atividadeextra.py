from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = 360, 640

class Login(BoxLayout):
    def __init__(self, **kwargs):
        Window.clearcolor = get_color_from_hex("#ffc1d5")
        super(Login, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [120, 200]
        self.spacing = 10

        self.add_widget(Image(source='6a87006a2e50cdacfd77020b8ad30868-removebg-preview.png', size_hint=(None,None),size=(210,120)))
        self.add_widget(Label(text='Login', font_size=35, font_name='Impact', color=get_color_from_hex('#d67FA1')))
        
        self.email_input = TextInput(hint_text="Email:", size_hint_y=None, height=40, background_color=get_color_from_hex('#F0E0E6'), multiline=False, font_size=20)
        self.add_widget(self.email_input)
        
        self.senha_input = TextInput(hint_text="Senha:", password=True, size_hint_y=None, height=40, background_color=get_color_from_hex('#F0E0E6'), multiline=False, font_size=20)
        self.add_widget(self.senha_input)

        self.button_login = Button(text='Login', background_color=('#FE70BD'), size_hint_y=None, height=40, font_size=20)
        self.add_widget(self.button_login)
        
        self.button_cadastrar = Button(text='Cadastro', background_color=('#FE70BD'), size_hint_y=None, height=40, font_size=20)
        self.add_widget(self.button_cadastrar)
        
        self.button_cadastrar.bind(on_press=self.cadastrar)  

    def cadastrar(self, *args):  
        App.get_running_app().root.current = 'Cadastro'  

class Cadastro(BoxLayout):
    def __init__(self, **kwargs):
        Window.clearcolor = get_color_from_hex("#ffc1d5")
        super(Cadastro, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [120, 250]
        self.spacing = 10

        self.add_widget(Label(text='Cadastre-se', font_size=35, font_name='Impact', color=get_color_from_hex('#d67FA1')))
        self.email_input = TextInput(hint_text="Email:", size_hint_y=None, height=40, background_color=get_color_from_hex('#F0E0E6'), multiline=False, font_size=20)
        self.add_widget(self.email_input)
        
        self.senha_input = TextInput(hint_text="Senha:", password=True, size_hint_y=None, height=40, background_color=get_color_from_hex('#F0E0E6'), multiline=False, font_size=20)
        self.add_widget(self.senha_input)

       
        self.button_cadastro = Button(text='Cadastrar', background_color=('#FE70BD'), size_hint_y=None, height=40, font_size=20)
        self.add_widget(self.button_cadastro)


class GerenciadorPg(App):
    def build(self):
        sm = ScreenManager()
        tela_login = Login()
        tela_cadastro = Cadastro()

        screen_login = Screen(name='Login')
        screen_cadastro = Screen(name='Cadastro')

        screen_login.add_widget(tela_login)
        screen_cadastro.add_widget(tela_cadastro)

        sm.add_widget(screen_login)
        sm.add_widget(screen_cadastro)

        return sm

if __name__ == '__main__':
    GerenciadorPg().run()
