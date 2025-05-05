import flet as ft
from components.ui_utils import create_text_field, create_button

class ForgotPasswordPage(ft.UserControl):
    def __init__(self, page, navigate_to):
        super().__init__()
        self.page = page
        self.navigate_to = navigate_to
        self.email_field = create_text_field("Email", icon=ft.icons.EMAIL)

    def reset_clicked(self, e):
        email = self.email_field.value
        if not email:
            self.page.snack_bar = ft.SnackBar(ft.Text("Vui lòng nhập email!"))
            self.page.snack_bar.open = True
        else:
            # TODO: Implement actual email sending logic
            self.page.snack_bar = ft.SnackBar(ft.Text(f"Liên kết đặt lại mật khẩu đã được gửi tới {email}"))
            self.page.snack_bar.open = True
            self.navigate_to(e, "login")
        self.page.update()

    def build(self):
        return ft.Column(
            [
                ft.Text("Quên mật khẩu", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                self.email_field,
                ft.Row(
                    [
                        create_button("Gửi liên kết", self.reset_clicked, icon=ft.icons.SEND),
                        create_button("Quay lại", lambda e: self.navigate_to(e, "login")),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        )