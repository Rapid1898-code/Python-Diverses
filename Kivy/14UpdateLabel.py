import time
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_file("14UpdateLabel.kv")

class MyLayout(Widget):
    def press(self):
        # Create variables for our widget
        name = self.ids.name_input.text

        self.ids.name_button.text = "Neuer Text"

        # Upate the label
        self.ids.name_label.text = name

        # Clear input box
        self.ids.name_input.text = ""

        time.sleep (2)

class AwesomeApp(App):
    def onStart(self):
        Clock.schedule_interval(self.updateWidget,0.5)
    def updateWidget(self,*args):
        print("Drinnen!")
        self.ids.name_input.text = self.ids.name_input.text.upper()
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
