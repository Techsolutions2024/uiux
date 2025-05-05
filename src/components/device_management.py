import flet as ft
from services.device_service import get_devices, add_device, delete_device
from components.ui_utils import create_button, create_text_field

class DeviceManagementPage(ft.UserControl):
    def __init__(self, page, navigate_to):
        super().__init__()
        self.page = page
        self.navigate_to = navigate_to
        self.device_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Tên")),
                ft.DataColumn(ft.Text("IP")),
                ft.DataColumn(ft.Text("Trạng thái")),
                ft.DataColumn(ft.Text("Hành động")),
            ],
            rows=[],
        )
        self.name_field = create_text_field("Tên Camera", emoji="📷")
        self.ip_field = create_text_field("Địa chỉ IP", emoji="🌐")
        self.load_devices()

    def load_devices(self):
        self.device_table.rows.clear()
        devices = get_devices()
        for device in devices:
            self.device_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(device["id"])),
                        ft.DataCell(ft.Text(device["name"])),
                        ft.DataCell(ft.Text(device["ip"])),
                        ft.DataCell(ft.Text("Online" if device["status"] else "Offline")),
                        ft.DataCell(
                            ft.Row(
                                [
                                    create_button("Xóa", lambda e, id=device["id"]: self.delete_device(id), emoji="🗑️"),
                                ]
                            )
                        ),
                    ]
                )
            )
        self.page.update()

    def add_device_clicked(self, e):
        name = self.name_field.value
        ip = self.ip_field.value
        if not name or not ip:
            self.page.snack_bar = ft.SnackBar(ft.Text("Vui lòng nhập đầy đủ thông tin!"))
            self.page.snack_bar.open = True
        else:
            add_device(name, ip)
            self.name_field.value = ""
            self.ip_field.value = ""
            self.load_devices()
            self.page.snack_bar = ft.SnackBar(ft.Text("Thêm camera thành công!"))
            self.page.snack_bar.open = True
        self.page.update()

    def delete_device(self, device_id):
        delete_device(device_id)
        self.load_devices()
        self.page.snack_bar = ft.SnackBar(ft.Text("Xóa camera thành công!"))
        self.page.snack_bar.open = True

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
                                ft.Text("Quản lý Thiết bị", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                create_button("Quay lại", lambda e: self.navigate_to(e, "dashboard"), emoji="⬅️"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            padding=20,
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Row(
                                        [
                                            self.name_field,
                                            self.ip_field,
                                            create_button("Thêm Camera", self.add_device_clicked, emoji="📷"),
                                        ],
                                        spacing=10,
                                    ),
                                    self.device_table,
                                ],
                                scroll=ft.ScrollMode.AUTO,
                            ),
                            padding=20,
                        ),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )