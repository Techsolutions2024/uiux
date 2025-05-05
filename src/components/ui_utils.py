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
        content=ft.Stack(
            [
                ft.Container(
                    content=ft.Image(
                        src="assets/images/ad.jpg",
                        width=1700,
                        height=500,
                        fit=ft.ImageFit.CONTAIN,
                        border_radius=10,
                    ),
                    left=0,
                    top=50,  # Dành chỗ cho tiêu đề
                ),
                ft.Container(
                    content=ft.Text(
                        "Quảng cáo Hệ thống Camera",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                    ),
                    left=600,  # Tọa độ x=10
                    top=10,   # Tọa độ y=10
                ),
                ft.Container(
                    content=ft.Text(
                        "Giám sát thông minh, an toàn tuyệt đối!",
                        size=16,
                        color=ft.colors.WHITE,
                        text_align=ft.TextAlign.LEFT,
                    ),
                    left=650,  # Tọa độ x=10
                    top=460,  # Tọa độ y=380 (dưới ảnh)
                ),
            ],
        ),
        width=1700,  # Phù hợp với ảnh
        height=460,  # Bao gồm ảnh và text
        alignment=ft.alignment.top_left,
        padding=0,
    )