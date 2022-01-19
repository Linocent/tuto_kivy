import os

from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.app import App


class Home(Screen):
    pass


class Thematics(Screen):
    rv_data = [{"elt": str(elt), "source": str("assets/hub_thematics/"+elt)}
               for elt in os.listdir("assets/hub_thematics") if elt.startswith("0")]


class Details(Screen):
    pass


class AnjacApp(App):
    bg = StringProperty()
    pTitle = StringProperty()

    def build(self):
        self.sm = self.root.ids["screen_manager"]

    def navPage(self, choice):
        self.sm.current = "details"
        choice = str(choice[0:-4])
        self.bg = f"assets/thematics/{choice}/background.png"
        self.pTitle = f"assets/thematics/{choice}/title.png"


anjac = AnjacApp()

if __name__ == "__main__":
    anjac.run()
