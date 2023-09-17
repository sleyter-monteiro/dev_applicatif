from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

Builder.load_file("action_bar.kv")

class BoxLayoutWithActionbar(BoxLayout):
    title = StringProperty("Title")