import flet as ft
import uuid

class Camera:
    def __init__(self, name, source_type, status, location):
        self.id = str(uuid.uuid4())
        self.name = name
        self.source_type = source_type
        self.status = status
        self.location = location

class CameraManagementApp:
    def __init__(self):
        self.cameras = [
            Camera("Cửa trước", "RTSP", "Online", "Cửa chính"),
            Camera("Kho hàng", "USB", "Offline", "Kho A"),
            Camera("Sân sau", "File", "Lỗi", "Sân sau"),
        ]
        self.new_camera_data = {
            "name": "",
            "location": "",
            "source_type": "RTSP",
            "url": "",
            "test_status": None
        }

    def __init__(self):
        self.cameras = [
            Camera("Cửa trước", "RTSP", "Online", "Cửa chính"),
            Camera("Kho hàng", "USB", "Offline", "Kho A"),
            Camera("Sân sau", "File", "Lỗi", "Sân sau"),
        ]
        self.new_camera_data = {
            "name": "",
            "location": "",
            "source_type": "RTSP",
            "url": "",
            "test_status": None
        }
        self.dialog = None

    def main(self, page: ft.Page):
        self.page = page
        page.title = "Hệ Thống Quản Lý Camera"
        page.window_width = 1000
        page.window_height = 600
        page.theme_mode = ft.ThemeMode.LIGHT
        page.padding = 20
        self.dialog = self.build_add_camera_dialog()
        self.show_main_view()
        page.update()

    def show_main_view(self):
        self.page.controls.clear()
        self.page.add(self.build_main_view())
        self.page.update()

    def build_main_view(self):
        def on_add_camera_click(e):
            self.new_camera_data = {"name": "", "location": "", "source_type": "RTSP", "url": "", "test_status": None}
            self.page.dialog = self.dialog
            self.dialog.open = True
            self.page.update()

        def on_edit_click(camera_id):
            print(f"Edit camera: {camera_id}")

        def on_config_click(camera_id):
            print(f"Configure camera: {camera_id}")

        def on_delete_click(camera_id):
            self.cameras = [cam for cam in self.cameras if cam.id != camera_id]
            self.show_main_view()

        def get_status_icon(status):
            if status == "Online":
                return "🟢"
            elif status == "Offline":
                return "🔴"
            return "🟡"

        rows = []
        for cam in self.cameras:
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(cam.name)),
                        ft.DataCell(ft.Text(cam.source_type)),
                        ft.DataCell(ft.Text(f"{get_status_icon(cam.status)} {cam.status}")),
                        ft.DataCell(ft.Text(cam.location)),
                        ft.DataCell(
                            ft.Row([
                                ft.IconButton(
                                    icon=ft.Icons.EDIT,
                                    tooltip="Sửa",
                                    on_click=lambda e, cid=cam.id: on_edit_click(cid)
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.SETTINGS,
                                    tooltip="Cấu hình",
                                    on_click=lambda e, cid=cam.id: on_config_click(cid)
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    tooltip="Xóa",
                                    on_click=lambda e, cid=cam.id: on_delete_click(cid)
                                ),
                            ])
                        ),
                    ]
                )
            )

        return ft.Column([
            ft.Text("🎦 DANH SÁCH CAMERA HIỆN TẠI", size=20, weight=ft.FontWeight.BOLD),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Thiết Bị")),
                    ft.DataColumn(ft.Text("Loại")),
                    ft.DataColumn(ft.Text("Trạng thái")),
                    ft.DataColumn(ft.Text("Vị trí")),
                    ft.DataColumn(ft.Text("Hành động")),
                ],
                rows=rows,
                border=ft.border.all(1, ft.Colors.GREY_400),
                divider_thickness=1,
            ),
            ft.Row([
                ft.TextField(label="🔍 Tìm kiếm", width=300),
                ft.Dropdown(
                    label="📂 Bộ lọc",
                    options=[ft.dropdown.Option("Tất cả"), ft.dropdown.Option("Online"), ft.dropdown.Option("Offline"), ft.dropdown.Option("Lỗi")],
                    value="Tất cả",
                    width=200
                ),
                ft.ElevatedButton("➕ Thêm Camera", on_click=on_add_camera_click),
            ], alignment=ft.MainAxisAlignment.START)
        ])

    def build_add_camera_dialog(self):
        device_name = ft.TextField(
            label="[B1] Nhập tên thiết bị",
            value=self.new_camera_data["name"],
            on_change=lambda e: self.new_camera_data.update({"name": e.control.value}),
            width=350,
            border_color=ft.Colors.BLUE_400
        )
        location = ft.TextField(
            label="[B2] Vị trí lắp đặt (tuỳ chọn)",
            value=self.new_camera_data["location"],
            on_change=lambda e: self.new_camera_data.update({"location": e.control.value}),
            width=350,
            border_color=ft.Colors.BLUE_400
        )
        source_type = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(value="RTSP", label="RTSP"),
                ft.Radio(value="File", label="File"),
                ft.Radio(value="USB", label="USB"),
            ]),
            value=self.new_camera_data["source_type"],
            on_change=lambda e: self.new_camera_data.update({"source_type": e.control.value})
        )
        url_input = ft.TextField(
            label="[B4] Nhập URL/Chọn file",
            value=self.new_camera_data["url"],
            on_change=lambda e: self.new_camera_data.update({"url": e.control.value}),
            width=350,
            border_color=ft.Colors.BLUE_400
        )
        test_status_text = ft.Text(
            f"➜ Trạng thái: {'✅ Thành công' if self.new_camera_data['test_status'] else '❌ Thất bại' if self.new_camera_data['test_status'] is False else 'Chưa kiểm tra'}",
            color=ft.Colors.GREY_600 if self.new_camera_data["test_status"] is None else (ft.Colors.GREEN_600 if self.new_camera_data["test_status"] else ft.Colors.RED_600)
        )
        preview_container = ft.Container(
            content=ft.Text("[B5] 🖥️ Preview khung nhỏ tại đây", italic=True, color=ft.Colors.GREY_600),
            width=320,
            height=180,
            bgcolor=ft.Colors.GREY_200,
            alignment=ft.alignment.center,
            border_radius=5
        )

        def on_test_click(e):
            self.new_camera_data["test_status"] = len(self.new_camera_data["url"]) > 10  # Giả lập test
            test_status_text.value = f"➜ Trạng thái: {'✅ Thành công' if self.new_camera_data['test_status'] else '❌ Thất bại'}"
            test_status_text.color = ft.Colors.GREEN_600 if self.new_camera_data["test_status"] else ft.Colors.RED_600
            if self.new_camera_data["test_status"]:
                preview_container.content = ft.Text("Preview video", color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER)
            self.page.update()

        def on_save_click(e):
            if all([self.new_camera_data["name"], self.new_camera_data["url"], self.new_camera_data["test_status"]]):
                self.cameras.append(Camera(
                    self.new_camera_data["name"],
                    self.new_camera_data["source_type"],
                    "Online" if self.new_camera_data["test_status"] else "Offline",
                    self.new_camera_data["location"]
                ))
                self.page.dialog.open = False
                self.show_main_view()
            else:
                self.page.show_snack_bar(ft.SnackBar(ft.Text("Vui lòng điền đầy đủ thông tin và kiểm tra kết nối!")))

        def on_back_click(e):
            self.page.dialog.open = False
            self.show_main_view()

        return ft.AlertDialog(
            title=ft.Text("➕ THÊM CAMERA MỚI", size=20, weight=ft.FontWeight.BOLD),
            content=ft.Column(
                [
                    device_name,
                    location,
                    ft.Text("[B3] Nguồn video:", size=14),
                    source_type,
                    url_input,
                    ft.ElevatedButton("🧪 Test Kết Nối", on_click=on_test_click),
                    test_status_text,
                    preview_container,
                ],
                spacing=10,
                width=400
            ),
            actions=[
                ft.TextButton("⏪ Quay lại", on_click=on_back_click),
                ft.ElevatedButton("💾 Lưu camera vào hệ thống", on_click=on_save_click),
            ],
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            content_padding=20
        )

if __name__ == "__main__":
    app = CameraManagementApp()
    ft.app(target=app.main)