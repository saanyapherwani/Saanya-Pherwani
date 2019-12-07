from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyApp(App): 
    def build(self): 
        self.app_window = GridLayout(cols = 2)
        self.button = Button(text = 'Click Me')         
        self.label = Label(text='')         
        self.button.bind(on_release = self.button_press) 
        self.app_window.add_widget(self.button)         
        self.app_window.add_widget(self.label) 
        return self.app_window
    def button_press(self,*args):
        self.label.text = 'Hello World'
        
if __name__ =='__main__': 
    MyApp().run()