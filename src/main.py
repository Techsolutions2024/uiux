import flet as ft
from components.login import LoginPage
from components.register import RegisterPage
from components.forgot_password import ForgotPasswordPage
from components.ui_utils import create_ad_container

def main(page: ft.Page):
    page.title = "Hệ thống Quản trị Camera"
    page.window.width = 1920
    page.window.height = 1080
    page.window.resizable = True
    page.padding = 0

    # Tạo layout chính: định vị form và quảng cáo theo pixel
    def navigate_to(e, route):
        form_container.content = None
        if route == "login":
            form_container.content = LoginPage(page, navigate_to)
        elif route == "register":
            form_container.content = RegisterPage(page, navigate_to)
        elif route == "forgot_password":
            form_container.content = ForgotPasswordPage(page, navigate_to)
        page.update()

    # Khung cố định cho form
    form_container = ft.Container(
        content=LoginPage(page, navigate_to),
        width=400,
        height=600,
        bgcolor=ft.colors.with_opacity(0.95, ft.colors.BLACK),
        border_radius=10,
        alignment=ft.alignment.center,
    )

    # Layout chính với gradient background toàn màn hình
    page.add(
        ft.Stack(
            [
                ft.Container(
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right,
                        colors=[
                            ft.colors.BLUE_300,
                            ft.colors.BLUE_700,
                            ft.colors.WHITE,
                        ],
                    ),
                    expand=True,
                ),
                ft.Container(
                    content=form_container,
                    left=50,
                    top=50,
                    height=600,
                    
                ),
                ft.Container(
                    content=create_ad_container(),
                    left=500,
                    top=50,
                ),
            ],
            expand=True,
        )
    )

ft.app(target=main)