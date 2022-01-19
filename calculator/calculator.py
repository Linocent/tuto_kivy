from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Calculate(GridLayout):
    def to_calculate(self, calculation):
        self.display.text = str(eval(calculation))


class CalculatorApp(App):
    def build(self):
        return Calculate()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
