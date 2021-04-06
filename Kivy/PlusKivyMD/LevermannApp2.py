from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string("LevermannApp2.kv")
        menu_items = [{"text": f"Item {i}"} for i in range(5)]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.dropdown_item,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item)

    def set_item(self, instance_menu, instance_menu_item):
        self.screen.ids.dropdown_item.set_item(instance_menu_item.text)
        instance_menu.dismiss()
    
    Window.size = (550, 700)    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file("LevermannApp2.kv")

    # def logger(self):
    #     self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'

    # def clear(self):
    #     self.root.ids.welcome_label.text = "WELCOME"
    #     self.root.ids.user.text = ""
    #     self.root.ids.password.text = ""                


MainApp().run()