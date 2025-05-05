import flet as ft

def create_icon(emoji, size=20):
    return ft.Text(emoji, size=size)

def create_button(text, on_click, emoji=None):
    return ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Text(emoji, size=20) if emoji else ft.Container(),
                ft.Text(text),
            ],
            spacing=5,
        ),
        bgcolor=ft.colors.BLUE_700,
        color=ft.colors.WHITE,
        on_click=on_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=10,
        ),
    )

def create_text_field(label, password=False, emoji=None):
    return ft.TextField(
        label=label,
        password=password,
        can_reveal_password=password,
        border_radius=8,
        prefix=ft.Text(emoji, size=20) if emoji else None,
        bgcolor=ft.colors.with_opacity(0.9, ft.colors.WHITE),
        border_color=ft.colors.BLUE_700,
    )

def create_ad_container():
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Quảng cáo Hệ thống Camera",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                ),
                ft.Image(
                    src="assets/images/ad.jpg",
                    width=350,
                    height=400,
                    fit=ft.ImageFit.COVER,
                    border_radius=10,
                ),
                ft.Text(
                    "Giám sát thông minh, an toàn tuyệt đối!",
                    size=16,
                    color=ft.colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        width=400,
        height=600,
        alignment=ft.alignment.center,
        padding=20,
    )