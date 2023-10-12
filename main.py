# main.py

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout

Builder.load_file("KivyApp.kv")

# Screen base
class MyScreenManager(ScreenManager):
    pass

# Different screens
class LoginScreen(Screen):
    def login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        if any(account["username"] == username and account["password"] == password for account in account_list):
            self.manager.current = "LoggedIn"

class Register(Screen):
    def create_account(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        account_list.append({"username": username, "password": password})

account_list = []

class LoggedIn(Screen):
    pass

# Layouts
class GridLayout(GridLayout):
    pass

class FloatLayout(FloatLayout):
    pass

class KivyApp(App):
    def build(self):
        return MyScreenManager()

KivyApp().run()
