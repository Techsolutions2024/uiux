import flet as ft
import re
from services.auth import register_user
from components.ui_utils import create_text_field, create_button
import flet as ft
import logging

logger = logging.getLogger("auth")

class RegisterPage:
    def __init__(self, page, navigate_to):
        self.page = page
        self.navigate_to = navigate_to
        self.name_field = create_text_field("Họ tên", emoji="🧑‍💼", on_change=self.on_name_change)
        self.email_field = create_text_field("Email", emoji="📧", on_change=self.on_email_change)
        self.password_field = create_text_field("Mật khẩu", password=True, emoji="🔐", on_change=self.on_password_change)
        self.confirm_password_field = create_text_field("Xác nhận mật khẩu", password=True, emoji="🔐", on_change=self.on_confirm_password_change)
        self.terms_agreement = ft.Checkbox(label="Đồng ý điều khoản sử dụng", value=False)

    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)

    def on_name_change(self, e):
        if e.control.value:
            e.control.color = ft.colors.PURPLE_700
        else:
            e.control.color = ft.colors.BLACK
        self.page.update()

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

    def on_confirm_password_change(self, e):
        if e.control.value:
            e.control.color = ft.colors.ORANGE_700
        else:
            e.control.color = ft.colors.BLACK
        self.page.update()

    def validate_password(self, password):
        # Password policy: at least 8 chars, one uppercase, one lowercase, one digit, one special char
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        return re.match(pattern, password)

    def register_clicked(self, e):
        name = self.name_field.value.strip()
        email = self.email_field.value.strip()
        password = self.password_field.value
        confirm_password = self.confirm_password_field.value
        if not all([name, email, password, confirm_password]):
            self.page.snack_bar = ft.SnackBar(ft.Text("Vui lòng nhập đầy đủ thông tin!"))
            self.page.snack_bar.open = True
        elif not self.validate_email(email):
            self.page.snack_bar = ft.SnackBar(ft.Text("Email không hợp lệ!"))
            self.page.snack_bar.open = True
        elif password != confirm_password:
            self.page.snack_bar = ft.SnackBar(ft.Text("Mật khẩu xác nhận không khớp!"))
            self.page.snack_bar.open = True
        elif not self.validate_password(password):
            self.page.snack_bar = ft.SnackBar(ft.Text("Mật khẩu phải có ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt!"))
            self.page.snack_bar.open = True
        elif not self.terms_agreement.value:
            self.page.snack_bar = ft.SnackBar(ft.Text("Vui lòng đồng ý điều khoản sử dụng!"))
            self.page.snack_bar.open = True
        else:
            if register_user(name, email, password):
                logger.info(f"User registered: {email}")
                self.page.snack_bar = ft.SnackBar(ft.Text("Đăng ký thành công!"))
                self.page.snack_bar.open = True
                self.navigate_to(e, "main")
            else:
                logger.warning(f"Failed registration attempt: {email} (email exists)")
                self.page.snack_bar = ft.SnackBar(ft.Text("Email đã tồn tại!"))
                self.page.snack_bar.open = True
        self.page.update()

    def build(self):
        return ft.Column(
            [
                ft.Text("Đăng ký", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                self.name_field,
                self.email_field,
                self.password_field,
                self.confirm_password_field,
                self.terms_agreement,
                ft.Row(
                    [
                        create_button("Đăng ký", self.register_clicked, emoji="🧑‍💼"),
                        create_button("Quay lại", lambda e: self.navigate_to(e, "login")),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        )
