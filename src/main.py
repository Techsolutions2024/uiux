import flet as ft
from flet import Colors
import logging
from ui.widgets import MainInterface
from components.login import LoginPage
from components.register import RegisterPage
from components.forgot_password import ForgotPasswordPage
from components.ui_utils import create_ad_container

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

def main(page: ft.Page):
    page.title = "Hệ thống Quản trị Camera"
    page.window.width = 1920
    page.window.height = 1080
    page.window.resizable = True
    page.padding = 0

    main_interface = None

    # Tạo layout chính: định vị form và quảng cáo theo pixel
    def navigate_to(e, route):
        nonlocal main_interface
        if route == "main":
            if main_interface is None:
                main_interface = MainInterface(page)
            # Clear current views and build main interface
            page.views.clear()
            page.controls.clear()
            main_interface.build()
        else:
            if main_interface is not None:
                # Clear main interface views if switching back to login/register
                page.views.clear()
                main_interface = None
            # Reset to login/register layout
            page.controls.clear()
            form_container.content = None
            if route == "login":
                form_container.content = LoginPage(page, navigate_to).build()
            elif route == "register":
                form_container.content = RegisterPage(page, navigate_to).build()
            elif route == "forgot_password":
                form_container.content = ForgotPasswordPage(page, navigate_to).build()
            page.controls.append(
                ft.Stack(
                    [
                        ft.Container(
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_left,
                                end=ft.alignment.bottom_right,
                                colors=[
                                    Colors.BLUE_300,
                                    Colors.BLUE_700,
                                    Colors.WHITE,
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
        page.update()

    # Khung cố định cho form
    form_container = ft.Container(
        content=LoginPage(page, navigate_to).build(),
        width=400,
        height=600,
        bgcolor=Colors.with_opacity(0.7, Colors.BLACK),
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
                            Colors.BLUE_300,
                            Colors.BLUE_700,
                            Colors.WHITE,
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