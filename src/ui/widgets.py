import flet as ft
import uuid

class MainInterface:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Phần Mềm Quản Lý Camera Tích Hợp AI"
        self.page.bgcolor = ft.colors.GREY_900
        self.page.fonts = {"Roboto": "https://github.com/google/fonts/raw/main/apache/roboto/Roboto%5Bwdth,wght%5D.ttf"}
        self.page.theme = ft.Theme(font_family="Roboto")
        self.page.padding = 0
        self.page.window_width = 1200
        self.page.window_height = 800

    def build(self):
        # Header
        header = ft.Container(
            content=ft.Row([
                ft.Image(src="https://via.placeholder.com/40", width=40, height=40),  # Logo
                ft.Text("Phần Mềm Quản Lý Camera Tích Hợp AI", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.Row([
                    ft.Text("Admin User", color=ft.colors.WHITE),
                    ft.TextButton("Đăng xuất", on_click=lambda e: self.page.window_close(), style=ft.ButtonStyle(color=ft.colors.RED_400))
                ], alignment=ft.MainAxisAlignment.END),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            bgcolor=ft.colors.BLUE_800,
            padding=10,
            height=60,
        )

        # Sidebar
        def create_menu_item(text, icon, color, route):
            return ft.Container(
                content=ft.Row([
                    ft.Icon(icon, color=ft.colors.WHITE),
                    ft.Text(text, color=ft.colors.WHITE, size=16),
                ]),
                bgcolor=color if self.page.route == route else ft.colors.GREY_800,
                padding=10,
                border_radius=5,
                margin=ft.margin.only(bottom=5),
                on_click=lambda e: self.page.go(route),
                tooltip=text,
            )

        sidebar = ft.Container(
            content=ft.Column([
                create_menu_item("Quản lý Thiết bị", ft.icons.DEVICES, ft.colors.BLUE_600, "/devices"),
                create_menu_item("Phân tích & Sự kiện AI", ft.icons.ANALYTICS, ft.colors.GREEN_600, "/analytics"),
                create_menu_item("Giám sát Trực tiếp", ft.icons.MONITOR, ft.colors.YELLOW_600, "/monitoring"),
                create_menu_item("Lưu trữ & Phát lại", ft.icons.STORAGE, ft.colors.PURPLE_600, "/storage"),
                create_menu_item("Bảo mật & Cài đặt", ft.icons.SECURITY, ft.colors.RED_600, "/security"),
                create_menu_item("Báo cáo & Phân tích", ft.icons.ASSESSMENT, ft.colors.TEAL_600, "/reports"),
                create_menu_item("Cảnh báo & Thông báo", ft.icons.WARNING, ft.colors.AMBER_600, "/alerts"),
                create_menu_item("Quản lý Người dùng", ft.icons.PEOPLE, ft.colors.INDIGO_600, "/users"),
                create_menu_item("Kiểm tra Trạng thái", ft.icons.CHECK_CIRCLE, ft.colors.CYAN_600, "/status"),
                create_menu_item("Tích hợp IoT", ft.icons.ROUTER, ft.colors.ORANGE_600, "/iot"),
                create_menu_item("Lịch sử hoạt động", ft.icons.HISTORY, ft.colors.PINK_600, "/history"),
            ], spacing=0),
            bgcolor=ft.colors.GREY_800,
            width=250,
            padding=10,
            expand=False,
        )

        # Main Content
        def create_user_management():
            return ft.Container(
                content=ft.Column([
                    ft.Text("Quản lý Người dùng", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Tên", color=ft.colors.WHITE)),
                            ft.DataColumn(ft.Text("Quyền", color=ft.colors.WHITE)),
                            ft.DataColumn(ft.Text("Hành động", color=ft.colors.WHITE)),
                        ],
                        rows=[
                            ft.DataRow(cells=[
                                ft.DataCell(ft.Text("User 1", color=ft.colors.WHITE)),
                                ft.DataCell(ft.Text("Admin", color=ft.colors.WHITE)),
                                ft.DataCell(ft.Row([
                                    ft.IconButton(ft.icons.EDIT, tooltip="Sửa", icon_color=ft.colors.BLUE_400,
                                                  on_click=lambda e: self.page.dialog.show()),
                                    ft.IconButton(ft.icons.DELETE, tooltip="Xóa", icon_color=ft.colors.RED_400,
                                                  on_click=lambda e: self.page.show_snack_bar(
                                                      ft.SnackBar(ft.Text("Xác nhận xóa?"), action="OK")))
                                ])),
                            ]),
                        ],
                        border=ft.border.all(1, ft.colors.GREY_700),
                    ),
                    ft.ElevatedButton("Thêm Người dùng", on_click=lambda e: self.page.dialog.show()),
                ], spacing=20),
                padding=20,
            )

        # Dialog for Add/Edit User
        def create_dialog():
            return ft.AlertDialog(
                title=ft.Text("Thêm/Sửa Người dùng"),
                content=ft.Column([
                    ft.TextField(label="Tên", bgcolor=ft.colors.GREY_800, color=ft.colors.WHITE),
                    ft.Dropdown(
                        label="Quyền",
                        options=[
                            ft.dropdown.Option("Admin"),
                            ft.dropdown.Option("User"),
                        ],
                        bgcolor=ft.colors.GREY_800,
                        color=ft.colors.WHITE,
                    ),
                ], tight=True),
                actions=[
                    ft.TextButton("Hủy", on_click=lambda e: self.page.dialog.close()),
                    ft.TextButton("Lưu", on_click=lambda e: self.page.dialog.close()),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )

        self.page.dialog = create_dialog()

        # Footer
        footer = ft.Container(
            content=ft.Row([
                ft.Text("Trạng thái: Hoạt động", color=ft.colors.WHITE),
                ft.Text("© 2025 Technology - AIot Camera Solutions - All Rights Reserved", color=ft.colors.WHITE),
                ft.TextButton("Hỗ trợ", style=ft.ButtonStyle(color=ft.colors.BLUE_400)),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            bgcolor=ft.colors.BLUE_800,
            padding=10,
            height=40,
        )

        # Routing
        def route_change(route):
            self.page.views.clear()
            self.page.views.append(
                ft.View(
                    route,
                    [
                        header,
                        ft.Row([
                            sidebar,
                            create_user_management() if self.page.route == "/users" else ft.Container(
                                content=ft.Text(f"Nội dung cho {self.page.route}", size=24, color=ft.colors.WHITE),
                                padding=20,
                                expand=True,
                            ),
                        ], expand=True),
                        footer,
                    ],
                    padding=0,
                    bgcolor=ft.colors.GREY_900,
                )
            )
            self.page.update()

        self.page.on_route_change = route_change
        self.page.go("/devices")