from kivy.app import kappa
from kivy.clock import Clock

class MainApp(App):
    def on_start(self):
        Clock.schedule_interval(self.update_label,2)
        Clock.schedule_one(self.foucs_text_input, 2)

    def update_label(self,*args):
        self.root.ids.counter.text = self.root.ids.counter.text + 1



MainApp().run()
