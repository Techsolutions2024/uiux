import flet as ft

def create_gradient_background():
    return ft.Container(
        content=ft.Stack(expand=True),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[
                ft.colors.BLUE_900,  # Màu xanh dương đậm
                ft.colors.PURPLE_900,  # Màu tím đậm
                ft.colors.BLUE_500,  # Màu xanh dương nhạt
            ],
        ),
        width=400,
        height=600,
    )

def create_icon(icon_name, color=ft.colors.WHITE):
    return ft.Icon(name=icon_name, color=color, size=20)

def create_button(text, on_click, icon=None):
    return ft.ElevatedButton(
        text=text,
        icon=icon,
        bgcolor=ft.colors.BLUE_700,
        color=ft.colors.WHITE,
        on_click=on_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=10,
        ),
    )

def create_text_field(label, password=False, icon=None):
    return ft.TextField(
        label=label,
        password=password,
        can_reveal_password=password,
        border_radius=8,
        prefix_icon=icon,
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
                    src="assets/images/ad_image.jpg",  # Thay bằng đường dẫn thực tế
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