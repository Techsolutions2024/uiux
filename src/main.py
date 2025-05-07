import flet as ft
from flet import Colors
import logging
from components.login import LoginPage
from components.register import RegisterPage
from components.forgot_password import ForgotPasswordPage
from components.ui_utils import create_ad_container
from ui.widgets import SidebarMenu, CameraWidget

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

    main_app_container = ft.Container()

    # Tạo layout chính: định vị form và quảng cáo theo pixel
    def navigate_to(e, route):
        form_container.content = None
        if route == "login":
            form_container.content = LoginPage(page, navigate_to).build()
        elif route == "register":
            form_container.content = RegisterPage(page, navigate_to).build()
        elif route == "forgot_password":
            form_container.content = ForgotPasswordPage(page, navigate_to).build()
        elif route == "main":
            # Build main app interface here
            main_app_container.content = ft.Row(
                [
                    SidebarMenu(on_select=lambda r: print(f"Selected menu: {r}")),
                    ft.Container(
                        content=ft.Text("Main app content goes here"),
                        expand=True,
                        padding=10,
                    ),
                ],
                expand=True,
            )
            form_container.content = main_app_container
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
