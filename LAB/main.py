from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.metrics import dp


class WidgetsExemple(GridLayout):
    compteur = 1
    compteur_actif = BooleanProperty(False)
    mon_texte = StringProperty("1")
    texte_input_str = StringProperty("input")
    # slider_value = StringProperty("Valeur")
    def on_button_click(self):
        print("Button clicked")
        if self.compteur_actif:
            self.compteur += 1
            self.mon_texte = str(self.compteur)
        else:
            print("Le compteur est désactivé")    
        
    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            widget.text = "ON" 
            self.compteur_actif = True
            
    def on_switch_active(self, widget):
        print("switch: " + str(widget.active))
    
    def on_slider_value(self, widget):
        print("slider: " + str(int(widget.value)))
        self.slider_value = str(int(widget.value))
        
    def on_text_validate(self, widget):
        print("validate: " + widget.text)
        self.texte_input_str = widget.text    

               



class MainWidget(Widget):
    pass


class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 500):
            b = Button(text=str(i+1), size_hint=(None, None))
            self.add_widget(b)

class GridLayoutExemple(GridLayout):
    pass


class AnchorLayoutExemple(AnchorLayout):
    pass


class BoxLayoutExemple(BoxLayout):
    pass
"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        self.add_widget(b1)
        b2 = Button(text="B")
        self.add_widget(b2)
        b3 = Button(text="C")
        self.add_widget(b3)
"""

class LeLabApp(App):
    pass



LeLabApp().run()