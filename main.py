from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty

class WidgetExample(GridLayout):
    count = 0
    toggle_enable = BooleanProperty(False)
    my_text= StringProperty('Hello')
    slider_value_txt = StringProperty("Value")
    text_intput_str = StringProperty("foo")
    def on_button_click(self):
        print("Hello")
        if self.toggle_enable:
            self.count +=1
            self.my_text = f"you clicked {self.count} times"

    def onclick_toggle_button(self,toggle):
        print(f"The toggle state is: {toggle.state}")
        if toggle.state == 'normal':
            toggle.text = 'OFF'
            self.toggle_enable =False
        else:
            toggle.text = "ON"
            self.toggle_enable =True

    # def on_switch_active(self,switch_data):
    #     print(type(switch_data.active))

    # def on_slider_value(slider_data):
    #     self.slider_value = 'true'
    def input_text_validate(self,widget):
        self.text_intput_str = widget.text

       
        

   

class MainWidgetApp(App):
    pass

MainWidgetApp().run()