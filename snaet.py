from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable


Window.size = (520, 900)


class MainApp(MDApp):
    def sin_login(self):

        self.root.ids.screen_man.current = "screen2"



    def rega(self, b):

        self.root.ids.screen_man.current = "screen2"



        self.root.ids.f2.add_widget(self.a)

    def registration(self):
        self.root.ids.screen_man.current = "screen3"





    def build(self):
        return Builder.load_file("aboba.kv")


MainApp().run()