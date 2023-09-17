from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty

Builder.load_file("widget_exemples.kv")

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