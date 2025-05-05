import flet as ft
from services.device_service import get_devices
from components.ui_utils import create_button

class LiveMonitoringPage(ft.UserControl):
    def __init__(self, page, navigate_to):
        super().__init__()
        self.page = page
        self.navigate_to = navigate_to
        self.camera_dropdown = ft.Dropdown(
            label="Chọn Camera",
            options=[ft.dropdown.Option(device["name"]) for device in get_devices()],
            width=300,
            bgcolor=ft.colors.with_opacity(0.9, ft.colors.WHITE),
            border_color=ft.colors.BLUE_700,
        )

    def ptz_control(self, direction):
        self.page.snack_bar = ft.SnackBar(ft.Text(f"PTZ: {direction}"))
        self.page.snack_bar.open = True
        self.page.update()

    def build(self):
        return ft.Stack(
            [
                ft.Container(
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right,
                        colors=[ft.colors.BLUE_300, ft.colors.BLUE_700, ft.colors.WHITE],
                    ),
                    expand=True,
                ),
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text("Giám sát Trực tiếp", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                create_button("Quay lại", lambda e: self.navigate_to(e, "dashboard"), emoji="⬅️"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            padding=20,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    self.camera_dropdown,
                                    ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.Image(
                                                    src="https://via.placeholder.com/400x300",
                                                    fit=ft.ImageFit.CONTAIN,
                                                    border_radius=10,
                                                ),
                                                width=400,
                                                height=300,
                                            ),
                                            ft.Container(
                                                content=ft.Image(
                                                    src="https://via.placeholder.com/400x300",
                                                    fit=ft.ImageFit.CONTAIN,
                                                    border_radius=10,
                                                ),
                                                width=400,
                                                height=300,
                                            ),
                                        ],
                                        spacing=20,
                                    ),
                                    ft.Row(
                                        [
                                            create_button("Lên", lambda e: self.ptz_control("Up"), emoji="⬆️"),
                                            create_button("Xuống", lambda e: self.ptz_control("Down"), emoji="⬇️"),
                                            create_button("Trái", lambda e: self.ptz_control("Left"), emoji="⬅️"),
                                            create_button("Phải", lambda e: self.ptz_control("Right"), emoji="➡️"),
                                            create_button("Zoom In", lambda e: self.ptz_control("Zoom In"), emoji="🔍+"),
                                            create_button("Zoom Out", lambda e: self.ptz_control("Zoom Out"), emoji="🔍-"),
                                        ],
                                        spacing=10,
                                    ),
                                ],
                                spacing=20,
                            ),
                            padding=20,
                        ),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )