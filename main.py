import flet as ft
from flet import *

def main(page: ft.Page):
    page.add()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)