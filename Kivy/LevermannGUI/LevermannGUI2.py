import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("LevermannScore2.kv")

class MyLayout(Widget):
    stockTicker = ObjectProperty(None)
    index = ObjectProperty(None)
    financeFlag = ObjectProperty(None)
    earningsDate = ObjectProperty(None)

    def levermannCalc(self):
        print(f"Levermann-Score Result: xyz")

class LevermannScore2(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    LevermannScore2().run()
