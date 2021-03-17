import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("14UpdateLabel.kv")

class MyLayout(Widget):
    def press(self):
        # Create variables for our widget
        name = self.ids.name_input.text

        # Upate the label
        self.ids.name_label.text = name

        # Clear input box
        self.ids.name_input.text = ""

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
