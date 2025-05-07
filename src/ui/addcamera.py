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
            "file": None,
            "test_status": None
        }

    def main(self, page: ft.Page):
        self.page = page
        page.title = "Hệ Thống Quản Lý Camera"
        page.window_width = 1000
        page.window_height = 600
        page.theme_mode = ft.ThemeMode.LIGHT
        page.padding = 20

        def show_main_view():
            page.controls.clear()
            page.add(self.build_main_view())
            page.update()

        def show_add_camera_wizard():
            page.controls.clear()
            page.add(self.build_add_camera_wizard())
            page.update()

        page.on_route_change = lambda e: (
            show_main_view() if page.route == "/main" else show_add_camera_wizard()
        )
        page.route = "/main"
        show_main_view()

    def build_main_view(self):
        def on_add_camera_click(e):
            self.new_camera_data = {"name": "", "location": "", "source_type": "RTSP", "url": "", "file": None, "test_status": None}
            self.page.route = "/add_camera"
            self.page.update()

        def on_edit_click(camera_id):
            print(f"Edit camera: {camera_id}")

        def on_config_click(camera_id):
            print(f"Configure camera: {camera_id}")

        def on_delete_click(camera_id):
            self.cameras = [cam for cam in self.cameras if cam.id != camera_id]
            self.page.controls.clear()
            self.page.add(self.build_main_view())
            self.page.update()

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
                                    icon=ft.icons.EDIT,
                                    tooltip="Sửa",
                                    on_click=lambda e, cid=cam.id: on_edit_click(cid)
                                ),
                                ft.IconButton(
                                    icon=ft.icons.SETTINGS,
                                    tooltip="Cấu hình",
                                    on_click=lambda e, cid=cam.id: on_config_click(cid)
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE,
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
                border=ft.border.all(1, ft.colors.GREY_400),
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

    def build_add_camera_wizard(self):
        def on_name_change(e):
            self.new_camera_data["name"] = e.control.value

        def on_location_change(e):
            self.new_camera_data["location"] = e.control.value

        def on_source_change(e):
            self.new_camera_data["source_type"] = e.control.value
            self.new_camera_data["url"] = ""
            self.new_camera_data["file"] = None
            self.new_camera_data["test_status"] = None
            update_input_field()

        def on_url_change(e):
            self.new_camera_data["url"] = e.control.value
            self.new_camera_data["file"] = None
            update_preview()

        def on_file_pick(e: ft.FilePickerResultEvent):
            if e.files:
                self.new_camera_data["file"] = e.files[0]
                self.new_camera_data["url"] = e.files[0].path
                url_field.value = e.files[0].name
                update_preview()
            else:
                self.new_camera_data["file"] = None
                self.new_camera_data["url"] = ""
                url_field.value = ""
                update_preview()
            self.page.update()

        def on_test_click(e):
            if self.new_camera_data["source_type"] == "File" and self.new_camera_data["file"]:
                self.new_camera_data["test_status"] = True  # Giả lập test file
            elif self.new_camera_data["url"]:
                self.new_camera_data["test_status"] = len(self.new_camera_data["url"]) > 10  # Giả lập test URL
            else:
                self.new_camera_data["test_status"] = False
            test_status_text.value = f"Trạng thái: {'✅ Thành công' if self.new_camera_data['test_status'] else '❌ Thất bại'}"
            update_save_button()
            self.page.update()

        def on_save_click(e):
            if all([self.new_camera_data["name"], self.new_camera_data["url"], self.new_camera_data["test_status"]]):
                self.cameras.append(Camera(
                    self.new_camera_data["name"],
                    self.new_camera_data["source_type"],
                    "Online" if self.new_camera_data["test_status"] else "Offline",
                    self.new_camera_data["location"]
                ))
                self.page.route = "/main"
                self.page.update()

        def on_back_click(e):
            self.page.route = "/main"
            self.page.update()

        def update_input_field():
            url_field.disabled = self.new_camera_data["source_type"] == "File"
            file_picker_button.visible = self.new_camera_data["source_type"] == "File"
            url_field.value = "" if self.new_camera_data["source_type"] == "File" else self.new_camera_data["url"]
            update_preview()
            self.page.update()

        def update_preview():
            if self.new_camera_data["source_type"] == "File" and self.new_camera_data["file"]:
                preview_content.content = ft.Text(f"File: {self.new_camera_data['file'].name}", italic=True)
            elif self.new_camera_data["url"]:
                preview_content.content = ft.Text(f"Luồng: {self.new_camera_data['url']}", italic=True)
            else:
                preview_content.content = ft.Text("🖥️ Chưa có luồng để xem trước", italic=True)
            self.page.update()

        def update_save_button():
            save_button.disabled = not all([self.new_camera_data["name"], self.new_camera_data["url"], self.new_camera_data["test_status"]])
            self.page.update()

        file_picker = ft.FilePicker(on_result=on_file_pick)
        self.page.overlay.append(file_picker)

        url_field = ft.TextField(
            label="URL/Chọn file",
            on_change=on_url_change,
            value=self.new_camera_data["url"],
            disabled=self.new_camera_data["source_type"] == "File"
        )

        file_picker_button = ft.ElevatedButton(
            "📂 Chọn File Video",
            on_click=lambda e: file_picker.pick_files(allowed_extensions=["mp4", "avi", "mkv"]),
            visible=self.new_camera_data["source_type"] == "File"
        )

        test_status_text = ft.Text(
            f"Trạng thái: {'✅ Thành công' if self.new_camera_data['test_status'] else '❌ Thất bại' if self.new_camera_data['test_status'] is False else 'Chưa kiểm tra'}"
        )

        preview_content = ft.Container(
            content=ft.Text("🖥️ Chưa có luồng để xem trước", italic=True),
            width=320,
            height=240,
            bgcolor=ft.colors.GREY_200,
            alignment=ft.alignment.center
        )

        save_button = ft.ElevatedButton("💾 Lưu", on_click=on_save_click, disabled=True)

        return ft.Column([
            ft.Text("➕ THÊM CAMERA MỚI", size=20, weight=ft.FontWeight.BOLD),
            ft.Container(
                content=ft.Column([
                    ft.TextField(label="Tên thiết bị", on_change=on_name_change, value=self.new_camera_data["name"]),
                    ft.TextField(label="Vị trí lắp đặt (tuỳ chọn)", on_change=on_location_change, value=self.new_camera_data["location"]),
                    ft.Dropdown(
                        label="Nguồn video",
                        options=[
                            ft.dropdown.Option("RTSP"),
                            ft.dropdown.Option("File"),
                            ft.dropdown.Option("USB")
                        ],
                        value=self.new_camera_data["source_type"],
                        on_change=on_source_change
                    ),
                    url_field,
                    file_picker_button,
                    ft.ElevatedButton("🧪 Test Kết Nối", on_click=on_test_click),
                    test_status_text,
                    ft.Text("Xem trước luồng video"),
                    preview_content
                ], spacing=10),
                padding=20,
                border=ft.border.all(1, ft.colors.GREY_400),
                border_radius=8
            ),
            ft.Row([
                ft.ElevatedButton("⏪ Quay lại", on_click=on_back_click),
                save_button
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        ])

if __name__ == "__main__":
    app = CameraManagementApp()
    ft.app(target=app.main)