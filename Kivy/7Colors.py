import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file("color.kv")

class MyGridLayout(Widget):
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        print(f"Hello {name}, you like {pizza} pizza, and your favorite color is {color}!")
        # self.add_widget (Label (text=f"Hello {name}, you like {pizza} pizza, and your favorite color is {color}!"))

class AwesomeApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    AwesomeApp().run()
