import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)
        self.cols = 1
        self.row_force_default=True
        self.row_default_height=120

        self.topGrid = GridLayout(
            row_force_default=True,
            row_default_height=40
        )
        self.topGrid.cols = 2

        self.topGrid.add_widget(Label(text="Stock: ",
                                      size_hint_y=None,
                                      height=50
                                      ))
        self.stock = TextInput(multiline=False,
                               size_hint_y=None,
                               height=50)
        self.topGrid.add_widget(self.stock)

        self.topGrid.add_widget(Label(text="Index: "))
        self.index = TextInput(multiline=False)
        self.topGrid.add_widget(self.index)

        self.topGrid.add_widget(Label(text="Finance Stock: "))
        self.financeFlag = TextInput(multiline=False)
        self.topGrid.add_widget(self.financeFlag)

        self.topGrid.add_widget(Label(text="Earnings Info: "))
        self.earningsInfo = TextInput(multiline=False)
        self.topGrid.add_widget(self.earningsInfo)

        self.add_widget (self.topGrid)

        self.submit = Button(text="Levermann Score",
                             font_size =32,
                             size_hint_y = None,
                             height = 50)
        self.submit.bind(on_press=self.levermannCalc)
        self.add_widget(self.submit)

    def levermannCalc(self,instance):
        self.add_widget (Label (text=f"Result: xyz"))


class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()
