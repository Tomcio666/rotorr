import kivy 
from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
import socket


def client(data):
    port = 5000

    client_soc = socket.socket()
    client_soc.connect(('127.0.0.1', port))
    client_soc.send(str(data).encode("utf-8"))
    client_soc.close()


class MainWidget(Widget):
    
    def __init__(self):
        super(MainWidget, self).__init__()
        self.angle = 0
        client(0)
        self.changeAngle('right')
        Builder.load_string('''
        <MainWidget>:
            BoxLayout:
                size: root.size
                orientation: "vertical"
                Label:
                    text: '''+f"'{self.angle}'"+'''
                GridLayout:
                    cols: 2

                    Button:
                        text: 'left'
                        on_press: root.changeAngle('left')
                    Button:
                        text: 'right'
                        on_press: root.changeAngle('right')
        ''')

    def changeAngle(self, dir):
        if dir == 'right':
            self.angle = 0 if self.angle == 359 else self.angle + 1
        elif dir == 'left':
            self.angle = 359 if self.angle == 0 else self.angle - 1

        client(dir)
        

class MyApp(App):
    def build(self):
        return MainWidget()



if __name__ == '__main__':
    MyApp().run()

