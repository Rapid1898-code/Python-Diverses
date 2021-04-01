from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

class MainApp(MDApp):
    Window.size = (550, 700)    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file("LevermannApp2.kv")

    # def logger(self):
    #     self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'

    # def clear(self):
    #     self.root.ids.welcome_label.text = "WELCOME"
    #     self.root.ids.user.text = ""
    #     self.root.ids.password.text = ""                


MainApp().run()