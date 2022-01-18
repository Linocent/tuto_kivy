from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class LoginScreen(Screen):
    def login(self):
        app.change_to('home')

    def wrong_id(self):
        self.error = "Wrong username or password, try again:"


class LoginBox(BoxLayout):
    """Take login and pass and lauch an event to the LoginScreen(Screen)"""
    __events__ = ('on_login_success', 'on_error')

    def on_login_success(self):
        pass

    def on_error(self):
        pass

    def to_log(self, username, password):
        app = App.get_running_app()

        if (username, password) == ("test", "1234"):
            self.dispatch('on_login_success')
            app.username = username

        self.dispatch('on_error')


class HomeScreen(Screen):
    """Second screen with log out button"""
    pass


class LogApp(App):
    username = StringProperty("")

    def build(self):
        self.sm = self.root.ids['screenmanager']

    def change_to(self, screen_name):
        self.sm.current = screen_name


if __name__ == "__main__":
    app = LogApp()
    app.run()
