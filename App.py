import kivy 
from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
import socket


def client(data):
    host = socket.gethostbyname()
    port = 5000

    client_soc = socket.socket()
    client_soc.connect((host,port))
    client_soc.send(data.encode())
    client_soc.close()


    Builder.load_string('''
    <MainWidget>:
        BoxLayout:
            size: root.size
            orientation: 'vertical'

            Label:
                text: str(root.angle)

            GridLayout:
                cols: 2

                Button:
                    text: 'left'
                    on_press: root.changeAngle('left')


    ''')


class MainWidget(BoxLayout):
    angle = NumericProperty()
    
    def __init__(self, dir):
        super(MainWidget, self).__init__(**kwargs)
    

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

    