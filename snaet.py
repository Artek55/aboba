from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivymd.uix.datatables import MDDataTable


Window.size = (520, 800)




class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MainApp(MDApp):
    def sin_login(self):

        self.root.ids.screen_man.current = "screen2"



    def rega(self):

        self.root.ids.screen_man.current = "screen2"


    def registration(self):
        self.root.ids.screen_man.current = "screen3"

    def back(self, screen):
        self.root.ids.screen_man.current = screen
        self.root.nav_drawer.set_state("close")
    def order1(self):
        self.root.ids.screen_man.current = "screen4"



    def order2(self):
        self.root.ids.screen_man.current = "screen5"

    def build(self):
        return Builder.load_file("aboba.kv")






MainApp().run()