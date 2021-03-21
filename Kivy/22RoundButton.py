import time
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_file("22RoundButton.kv")

class MyLayout(Widget):
    def spinner_clicked(self,value):
        self.ids.click_label.text = f"You selected: {value}"

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
