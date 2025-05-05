import flet as ft
from components.ui_utils import create_card
from components.device_management import DeviceManagementPage
from components.live_monitoring import LiveMonitoringPage

class DashboardPage(ft.UserControl):
    def __init__(self, page, navigate_to):
        super().__init__()
        self.page = page
        self.navigate_to = navigate_to

    def navigate_to_module(self, e, module):
        self.page.controls.clear()
        if module == "device_management":
            self.page.add(DeviceManagementPage(self.page, self.navigate_to))
        elif module == "live_monitoring":
            self.page.add(LiveMonitoringPage(self.page, self.navigate_to))
        # TODO: Thêm các module khác
        self.page.update()

    def build(self):
        return ft.Stack(
            [
                ft.Container(
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right,
                        colors=[ft.colors.BLUE_300, ft.colors.BLUE_700, ft.colors.WHITE],
                    ),
                    expand=True,
                ),
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text("Hệ thống Quản trị Camera", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                ft.ElevatedButton("Đăng xuất", on_click=lambda e: self.navigate_to(e, "login"), bgcolor=ft.colors.BLUE_700, color=ft.colors.WHITE),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            padding=20,
                        ),
                        ft.Container(
                            content=ft.Row(
                                [
                                    create_card("Quản lý Thiết bị", "Quản lý camera, cảm biến", "📷", lambda e: self.navigate_to_module(e, "device_management")),
                                    create_card("Phân tích & Sự kiện AI", "Nhận diện, cảnh báo", "🧠", None),
                                    create_card("Quản lý Người dùng", "Phân quyền, log, 2FA", "👤", None),
                                    create_card("Giám sát Trực tiếp", "Live view, PTZ", "📺", lambda e: self.navigate_to_module(e, "live_monitoring")),
                                    create_card("Lưu trữ & Phát lại", "Video, metadata", "💾", None),
                                    create_card("Bảo mật & Cài đặt", "Mã hóa, backup, audit", "🔒", None),
                                    create_card("Báo cáo & Phân tích", "Dashboard, dự đoán", "📊", None),
                                    create_card("Cảnh báo & Thông báo", "Email, SMS, app", "🔔", None),
                                    create_card("Tích hợp & Tùy chỉnh", "ONVIF, RESTful, SDK", "🔌", None),
                                ],
                                wrap=True,
                                spacing=20,
                                run_spacing=20,
                            ),
                            padding=20,
                        ),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )