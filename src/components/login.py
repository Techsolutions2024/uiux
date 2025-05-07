import flet as ft
import re
from services.auth import authenticate_user
from components.ui_utils import create_text_field, create_button
import flet as ft
import logging

logger = logging.getLogger("auth")

class LoginPage:
    def __init__(self, page, navigate_to):
        self.page = page
        self.navigate_to = navigate_to
        self.email_field = create_text_field("Email", emoji="📧", on_change=self.on_email_change)
        self.password_field = create_text_field("Mật khẩu", password=True, emoji="🔐", on_change=self.on_password_change)
        self.remember_me = ft.Checkbox(label="Ghi nhớ đăng nhập", value=False)

    def validate_email(self, email):
        # Basic email regex validation
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)

    def on_email_change(self, e):
        if e.control.value:
            e.control.color = ft.colors.BLUE_700
        else:
            e.control.color = ft.colors.BLACK
        self.page.update()

    def on_password_change(self, e):
        if e.control.value:
            e.control.color = ft.colors.GREEN_700
        else:
            e.control.color = ft.colors.BLACK
        self.page.update()

    def login_clicked(self, e):
        email = self.email_field.value.strip()
        password = self.password_field.value
        if not email or not password:
            self.page.snack_bar = ft.SnackBar(ft.Text("Vui lòng nhập đầy đủ thông tin!"))
            self.page.snack_bar.open = True
            self.page.update()
            return
        if not self.validate_email(email):
            self.page.snack_bar = ft.SnackBar(ft.Text("Email không hợp lệ!"))
            self.page.snack_bar.open = True
            self.page.update()
            return
        if authenticate_user(email, password):
            logger.info(f"User logged in: {email}")
            self.page.snack_bar = ft.SnackBar(ft.Text("Đăng nhập thành công!"))
            self.page.snack_bar.open = True
            self.navigate_to(e, "main")
        else:
            logger.warning(f"Failed login attempt: {email}")
            self.page.snack_bar = ft.SnackBar(ft.Text("Email hoặc mật khẩu không đúng!"))
            self.page.snack_bar.open = True
        self.page.update()

    def build(self):
        return ft.Column(
            [
                ft.Text("Đăng nhập", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_400),
                self.email_field,
                self.password_field,
                self.remember_me,
                ft.Row(
                    [
                        create_button("Đăng nhập", self.login_clicked, emoji="🔐"),
                        create_button("Quên MK?", lambda e: self.navigate_to(e, "forgot_password")),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.TextButton(
                    "Chưa có tài khoản? Đăng ký ngay",
                    on_click=lambda e: self.navigate_to(e, "register"),
                    style=ft.ButtonStyle(color=ft.colors.BLUE_400),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        )
