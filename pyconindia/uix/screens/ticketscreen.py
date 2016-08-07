from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button


class TicketScreen(Screen): 
    Builder.load_string("""<TicketScreen>
    name: 'TicketScreen'
    BoxLayout
        padding: dp(12)
        orientation: 'vertical'
        spacing:dp(5)
        Button
            default: True
            text: 'My tickets'
            size_hint_y: None
            height: dp(54)
            color: app.base_inactive_color
            on_release:
                import webbrowser
                webbrowser.open('http://in.explara.com/a/account/manage/my-orders')
        Button
            default: True
            text: 'Buy tickets'
            size_hint_y: None
            height: dp(54)
            color: app.base_inactive_color
            on_release:
                import webbrowser
                webbrowser.open('https://in.explara.com/e/pycon-india-2016')
        """)
