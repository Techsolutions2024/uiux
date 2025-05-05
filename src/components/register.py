import flet as ft
from services.auth import register_user
from components.ui_utils import create_text_field, create_button

class RegisterPage(ft.UserControl):
    def __init__(self, page, navigate_to):
        super().__init__()
        self.page = page
        self.navigate_to = navigate_to
        self.name_field = create_text_field("Họ tên", icon=ft.icons.PERSON)
        self.email_field = create_text_field("Email", icon=ft.icons.EMAIL)
        self.password_field = create_text_field("Mật khẩu", password=True, icon=ft.icons.LOCK)
        self.confirm_password_field = create_text_field("Xác nhận mật khẩu", password=True, icon=ft.icons.LOCK)
        self.terms_agreement = ft.Checkbox(label="Đồng ý điều khoản sử dụng", value=False)

    def register_clicked(self, e):
        name = self.name_field.value
        email = self.email_field.value
        password = self.password_field.value
        confirm_password = self.confirm_password_field.value
        if not all([name, email, password, confirm_password]):
            self.page.snack_bar = ft.SnackBar(ft.Text("Vui lòng nhập đầy đủ thông tin!"))
            self.page.snack_bar.open = True
        elif password != confirm_password:
            self.page.snack_bar = ft.SnackBar(ft.Text("Mật khẩu xác nhận không khớp!"))
            self.page.snack_bar.open = True
        elif not self.terms_agreement.value:
            self.page.snack_bar = ft.SnackBar(ft.Text("Vui lòng đồng ý điều khoản sử dụng!"))
            self.page.snack_bar.open = True
        else:
            if register_user(name, email, password):
                self.page.snack_bar = ft.SnackBar(ft.Text("Đăng ký thành công!"))
                self.page.snack_bar.open = True
                self.navigate_to(e, "login")
            else:
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
                        create_button("Đăng ký",  create_button("Đăng ký", self.register_clicked, icon=ft.icons.PERSON_ADD)),
                        create_button("Quay lại", lambda e: self.navigate_to(e, "login")),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        )