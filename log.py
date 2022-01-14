import kivy

from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty


class Log(Screen):
    """First screen where user write username and password"""
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    info = ObjectProperty(None)

    def check_user(self):
        """Check if the user's info are right"""
        if (self.username.text, self.password.text) == ("test", "1234"):
            log.login(self.username.text)
            self.reset()
        else:
            self.info.text = "Wrong username or password, try again:"
            self.info.color = "#EC0707"
            self.username.text = ""
            self.password.text = ""

    def reset(self):
        """Reset username and password"""
        self.username.text = ""
        self.password.text = ""


class Home(Screen):
    """Second screen with log out button"""
    pass


class LogApp(App):
    username = StringProperty("")

    def build(self):
        self.sm = self.root.ids['screen_manager']

    def login(self, username):
        self.sm.current = "home"
        self.username = f" Hello {username}"


log = LogApp()

if __name__ == "__main__":
    log.run()
