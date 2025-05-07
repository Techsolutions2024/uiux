import flet as ft
from ui.widgets import SidebarMenu, CameraWidget

def main(page: ft.Page):
    page.title = "Test Widgets"
    page.window_width = 900
    page.window_height = 600

    def on_menu_select(route):
        page.snack_bar = ft.SnackBar(ft.Text(f"Selected menu: {route}"))
        page.snack_bar.open = True
        page.update()

    sidebar = SidebarMenu(on_select=on_menu_select)

    camera_widget = CameraWidget(
        camera_name="Camera 1",
        camera_status="connected",
        in_count=10,
        out_count=5,
        total_count=15,
        object_type="Person",
        on_click_callback=lambda name: print(f"Clicked on {name}")
    )

    page.add(
        ft.Row(
            [
                sidebar,
                ft.Container(width=20),  # spacer
                camera_widget,
            ],
            expand=True,
        )
    )

ft.app(target=main)
