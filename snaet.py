from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
Window.size = (520, 800)




class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MainApp(MDApp):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #
    #     menu_items = [
    #         {
    #             "viewclass": "IconListItem",
    #             "icon": "git",
    #             "height": dp(56),
    #             "text": f"Item {i}",
    #             "on_release": lambda x=f"Item {i}": self.set_item(x),
    #         } for i in range(5)]
    #     self.menu = MDDropdownMenu(
    #         caller=self.screen.ids.field,
    #         items=menu_items,
    #         position="bottom",
    #         width_mult=4,
    #   )
    def sin_login(self):

        self.root.ids.screen_man.current = "screen2"

    # def open_menu_list(self):
    #     class MainApp(MDApp):
    #         def __init__(self, **kwargs):
    #             super().__init__(**kwargs)
    #
    #             menu_items = [
    #                 {
    #                     "viewclass": "IconListItem",
    #                     "icon": "git",
    #                     "height": dp(56),
    #                     "text": f"Item {i}",
    #                     "on_release": lambda x=f"Item {i}": self.set_item(x),
    #                 } for i in range(5)]
    #             self.menu = MDDropdownMenu(
    #                 caller=self.screen.ids.field,
    #                 items=menu_items,
    #                 position="bottom",
    #                 width_mult=4,
    #             )







    def menu_callback(self):
        pass

    def rega(self):

        self.root.ids.screen_man.current = "screen2"


    def registration(self):
        self.root.ids.screen_man.current = "screen3"

    def back(self, screen):
        self.root.ids.screen_man.current = screen
        self.root.nav_drawer.set_state("close")
    def order1(self):
        self.root.nav_drawer.set_state("close")
        self.root.ids.screen_man.current = "screen4"



    def order2(self):
        self.root.ids.screen_man.current = "screen5"


    def set(self):
        self.root.ids.screen_man.current = "screen6"

    def flower(self):
        self.root.ids.screen_man.current = "screen7"


    def set1(self):
        self.root.ids.screen_man.current = "screen8"

    def flower1(self):
        self.root.ids.screen_man.current = "screen9"







    def build(self):
        return Builder.load_file("aboba.kv")







MainApp().run()