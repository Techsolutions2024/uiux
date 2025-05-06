import flet as ft
import re
import logging
from components.ui_utils import create_text_field, create_button
from services.auth import send_password_reset_email

logger = logging.getLogger("auth")

class ForgotPasswordPage:
    def __init__(self, page, navigate_to):
        self.page = page
        self.navigate_to = navigate_to
        self.email_field = create_text_field("Email", emoji="📧")

    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)

    def reset_clicked(self, e):
        email = self.email_field.value.strip()
        if not email:
            self.page.snack_bar = ft.SnackBar(ft.Text("Vui lòng nhập email!"))
            self.page.snack_bar.open = True
        elif not self.validate_email(email):
            self.page.snack_bar = ft.SnackBar(ft.Text("Email không hợp lệ!"))
            self.page.snack_bar.open = True
        else:
            # Call service to send password reset email with token
            if send_password_reset_email(email):
                logger.info(f"Password reset email sent to: {email}")
                self.page.snack_bar = ft.SnackBar(ft.Text(f"Liên kết đặt lại mật khẩu đã được gửi tới {email}"))
                self.page.snack_bar.open = True
                self.navigate_to(e, "login")
            else:
                logger.warning(f"Password reset requested for non-existent email: {email}")
                self.page.snack_bar = ft.SnackBar(ft.Text("Email không tồn tại trong hệ thống!"))
                self.page.snack_bar.open = True
        self.page.update()

    def build(self):
        return ft.Column(
            [
                ft.Text("Quên mật khẩu", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                self.email_field,
                ft.Row(
                    [
                        create_button("Gửi liên kết", self.reset_clicked, emoji="📨"),
                        create_button("Quay lại", lambda e: self.navigate_to(e, "login")),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        )
