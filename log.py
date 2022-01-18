from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class LoginScreen(Screen):
    def change(self):
        self.manager.current = "home"


class LoginBox(BoxLayout):
    """Take login and pass and lauch an event to the LoginScreen(Screen)"""
    __events__ = ('on_login_success', 'on_error')

    def on_login_success(self):
        pass

    def on_error(self):
        pass

    def get_data(self):
        fields_user = self.ids.username
        fields_password = self.ids.password
        for fields in reversed(fields_user.children):
            for n in fields.children:
                if isinstance(n, TextInput):
                    username = n.text
                    n.text = ""
        for fields in reversed(fields_password.children):
            for m in fields.children:
                if isinstance(m, TextInput):
                    password = m.text
                    m.text = ""
        self.to_log(username, password)

    def to_log(self, username, password):
        if (username, password) == ("test", "1234"):
            self.dispatch('on_login_success')
            log.username = username
            self.reset()
        else:
            self.dispatch('on_error')

    def reset(self):
        """Reset username and password"""
        self.ids["username"].text = ""
        self.ids["password"].text = ""


class Home(Screen):
    """Second screen with log out button"""
    pass


class LogApp(App):
    username = StringProperty("")

    def build(self):
        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="log"))
        sm.add_widget(Home(name="home"))
        return sm


log = LogApp()

if __name__ == "__main__":
    log.run()
