from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen
import pyrebase
from kivy.clock import Clock
from kivy.uix.image import Image

Window.size = 360, 640

config = {
    "apiKey": "AIzaSyDwYy9yX5utlnt2QmdNxMx6f_gn25xhE68",
    "authDomain": "cadastro-cfb8b.firebaseapp.com",
    "databaseURL": "https://cadastro-cfb8b-default-rtdb.firebaseio.com",
    "projectId": "cadastro-cfb8b",
    "storageBucket": "cadastro-cfb8b.appspot.com",
    "messagingSenderId": "1028739319536",
    "appId": "1:1028739319536:web:85b4e2de4559d02afd6435",
    "measurementId": "G-15LP4MHTP2"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

class Login(BoxLayout):
    def __init__(self, **kwargs):
        Window.clearcolor = get_color_from_hex("#ffc1d5")
        super(Login, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [120, 200]
        self.spacing = 10

        self.add_widget(Image(source='6a87006a2e50cdacfd77020b8ad30868-removebg-preview.png', size_hint=(None,None),size=(210,120)))
        self.message_label = Label(text='', color=get_color_from_hex('#FF0000'), font_size=16)
        self.add_widget(self.message_label)

        self.add_widget(Label(text='Login', font_size=35, font_name='Impact', color=get_color_from_hex('#d67FA1')))
        
        self.email_input = TextInput(hint_text="Email:", size_hint_y=None, height=40, background_color=get_color_from_hex('#F0E0E6'), multiline=False, font_size=20)
        self.add_widget(self.email_input)
        
        self.senha_input = TextInput(hint_text="Senha:", password=True, size_hint_y=None, height=40, background_color=get_color_from_hex('#F0E0E6'), multiline=False, font_size=20)
        self.add_widget(self.senha_input)

        self.button_login = Button(text='Login', background_color=('#FE70BD'), size_hint_y=None, height=40, font_size=20)
        self.add_widget(self.button_login)
        self.button_login.bind(on_press=self.login)

        self.button_cadastrar = Button(text='Cadastro', background_color=('#FE70BD'), size_hint_y=None, height=40, font_size=20)
        self.add_widget(self.button_cadastrar)
        self.button_cadastrar.bind(on_press=self.cadastrar)

    def login(self, *args):
        try:
            user = auth.sign_in_with_email_and_password(self.email_input.text, self.senha_input.text)
            print("Login bem-sucedido")
            self.message_label.text = 'Login bem-sucedido!'
            self.message_label.color = get_color_from_hex('#008000')  # verde
            self.message_label.font_size = 20
            # Redireciona para a tela principal após um segundo (para dar tempo de visualizar a mensagem)
            Clock.schedule_once(lambda dt: setattr(App.get_running_app().root, 'current', 'Principal'), 5)
        except Exception as e:
            print(f"Login falhou: {str(e)}")
            self.message_label.text = 'Dados inválidos'
            self.message_label.color = get_color_from_hex('#FF0000')  # vermelho

    def cadastrar(self, *args):
        App.get_running_app().root.current = 'Cadastro'

class Cadastro(BoxLayout):
    def __init__(self, **kwargs):
        Window.clearcolor = get_color_from_hex("#ffc1d5")
        super(Cadastro, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [120, 250]
        self.spacing = 10

        self.message_label = Label(text='', color=get_color_from_hex('#FF0000'), font_size=16)
        self.add_widget(self.message_label)

        self.add_widget(Label(text='Cadastre-se', font_size=35, font_name='Impact', color=get_color_from_hex('#d67FA1')))
        
        self.email_input = TextInput(hint_text="Email:", size_hint_y=None, height=40, background_color=get_color_from_hex('#F0E0E6'), multiline=False, font_size=20)
        self.add_widget(self.email_input)
        
        self.senha_input = TextInput(hint_text="Senha:", password=True, size_hint_y=None, height=40, background_color=get_color_from_hex('#F0E0E6'), multiline=False, font_size=20)
        self.add_widget(self.senha_input)

        self.button_cadastro = Button(text='Cadastrar', background_color=('#FE70BD'), size_hint_y=None, height=40, font_size=20)
        self.add_widget(self.button_cadastro)
        self.button_cadastro.bind(on_press=self.cadastrar)

    def cadastrar(self, *args):
        try:
            user = auth.create_user_with_email_and_password(self.email_input.text, self.senha_input.text)
            print("Cadastro bem-sucedido")
            self.message_label.text = 'Cadastro realizado com sucesso!'
            self.message_label.color = get_color_from_hex('#008000')  # verde
            self.message_label.font_size = 20
            # Redireciona para a tela de login após um segundo (para dar tempo de visualizar a mensagem)
            Clock.schedule_once(lambda dt: setattr(App.get_running_app().root, 'current', 'Login'), 5)
        except Exception as e:
            print(f"Cadastro falhou: {str(e)}")
            self.message_label.text = 'Erro ao cadastrar'
            self.message_label.color = get_color_from_hex('#FF0000')  # vermelho

class Principal(BoxLayout):
    def __init__(self, **kwargs):
        Window.clearcolor = get_color_from_hex("#ffc1d5")
        super(Principal, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [120, 200]
        self.spacing = 10

        self.add_widget(Label(text='Bem-vindo!', font_size=35, font_name='Impact', color=get_color_from_hex('#d67FA1')))

class GerenciadorPg(App):
    def build(self):
        sm = ScreenManager()
        tela_login = Login()
        tela_cadastro = Cadastro()
        tela_principal = Principal()

        screen_login = Screen(name='Login')
        screen_cadastro = Screen(name='Cadastro')
        screen_principal = Screen(name='Principal')

        screen_login.add_widget(tela_login)
        screen_cadastro.add_widget(tela_cadastro)
        screen_principal.add_widget(tela_principal)

        sm.add_widget(screen_login)
        sm.add_widget(screen_cadastro)
        sm.add_widget(screen_principal)

        return sm

if __name__ == '__main__':
    GerenciadorPg().run()



