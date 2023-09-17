from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from nav import NavScreenManager
from kivy.metrics import dp

class MyScreenManager(NavScreenManager):
    pass

class LeLabApp(App):
    manager = ObjectProperty(None)
    
    def build(self):
        self.manager = MyScreenManager()
        return self.manager



LeLabApp().run()