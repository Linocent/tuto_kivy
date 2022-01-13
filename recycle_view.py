from kivy.uix.recycleview import RecycleView
from kivy.app import App


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(10)]


class TestApp(App):
    def build(self):
        return RV()


test = TestApp()

if __name__ == "__main__":
    test.run()