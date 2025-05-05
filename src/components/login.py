import flet as ft
from services.auth import authenticate_user
from components.ui_utils import create_text_field, create_button, create_icon

class LoginPage(ft.UserControl):
    def __init__(self, page, navigate_to):
        super().__init__()
        self.page = page
        self.navigate_to = navigate_to
        self.email_field = create_text_field("Email", icon=ft.icons.EMAIL)
        self.password_field = create_text_field("Mật khẩu", password=True, icon=ft.icons.LOCK)
        self.remember_me = ft.Checkbox(label="Ghi nhớ đăng nhập", value=False)

    def login_clicked(self, e):
        email = self.email_field.value
        password = self.password_field.value
        if not email or not password:
            self.page.snack_bar = ft.SnackBar(ft.Text("Vui lòng nhập đầy đủ thông tin!"))
            self.page.snack_bar.open = True
            self.page.update()
            return
        if authenticate_user(email, password):
            self.page.snack_bar = ft.SnackBar(ft.Text("Đăng nhập thành công!"))
            self.page.snack_bar.open = True
            # TODO: Navigate to main app dashboard
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Email hoặc mật khẩu không đúng!"))
            self.page.snack_bar.open = True
        self.page.update()

    def build(self):
        return ft.Column(
            [
                ft.Text("Đăng nhập", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                self.email_field,
                self.password_field,
                self.remember_me,
                ft.Row(
                    [
                        create_button("Đăng nhập", self.login_clicked, icon=ft.icons.LOGIN),
                        create_button("Quên MK?", lambda e: self.navigate_to(e, "forgot_password")),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.TextButton(
                    "Chưa có tài khoản? Đăng ký ngay",
                    on_click=lambda e: self.navigate_to(e, "register"),
                    style=ft.ButtonStyle(color=ft.colors.WHITE),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        )