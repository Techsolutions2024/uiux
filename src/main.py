import flet as ft
from components.login import LoginPage
from components.register import RegisterPage
from components.forgot_password import ForgotPasswordPage
from components.ui_utils import create_ad_container

def main(page: ft.Page):
    page.title = "Hệ thống Quản trị Camera"
    page.window.width = 800
    page.window.height = 600
    page.window.resizable = True
    page.padding  # Tắt padding mặc định
    page.bgcolor = ft.colors.TRANSPARENT

    # Tạo layout chính: bên trái là form, bên phải là quảng cáo
    def navigate_to(e, route):
        form_container.content = None
        if route == "login":
            form_container.content = LoginPage(page, navigate_to)
        elif route == "register":
            form_container.content = RegisterPage(page, navigate_to)
        elif route == "forgot_password":
            form_container.content = ForgotPasswordPage(page, navigate_to)
        page.update()

    # Khung cố định cho form (bên trái)
    form_container = ft.Container(
        content=LoginPage(page, navigate_to),
        width=400,
        height=600,
        bgcolor=ft.colors.with_opacity(0.95, ft.colors.BLACK),
        border_radius=10,
        alignment=ft.alignment.center,
    )

    # Layout chính với background image
    page.add(
        ft.Container(
            content=ft.Row(
                [
                    form_container,  # Form cố định bên trái
                    create_ad_container(),  # Quảng cáo bên phải
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.START,
            ),
            image_src="assets/images/background.jpg",
            image_fit=ft.ImageFit.COVER,
            width=800,
            height=600,
        )
    )

ft.app(target=main)