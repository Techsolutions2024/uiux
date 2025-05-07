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
        self.current_step = 1
        self.new_camera_data = {
            "name": "",
            "location": "",
            "source_type": "RTSP",
            "url": "",
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
            self.current_step = 1
            self.new_camera_data = {"name": "", "location": "", "source_type": "RTSP", "url": "", "test_status": None}
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
        def update_step():
            wizard_content.controls.clear()
            if self.current_step == 1:
                wizard_content.controls.append(self.build_step_1())
            elif self.current_step == 2:
                wizard_content.controls.append(self.build_step_2())
            elif self.current_step == 3:
                wizard_content.controls.append(self.build_step_3())
            elif self.current_step == 4:
                wizard_content.controls.append(self.build_step_4())
            elif self.current_step == 5:
                wizard_content.controls.append(self.build_step_5())
            self.page.update()

        def on_back_click(e):
            if self.current_step > 1:
                self.current_step -= 1
                update_step()
            else:
                self.page.route = "/main"
                self.page.update()

        def on_next_click(e):
            if self.current_step < 5:
                self.current_step += 1
                update_step()

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

        wizard_content = ft.Column([])

        update_step()

        return ft.Column([
            ft.Text("➕ THÊM CAMERA MỚI", size=20, weight=ft.FontWeight.BOLD),
            ft.Container(
                content=wizard_content,
                padding=20,
                border=ft.border.all(1, ft.colors.GREY_400),
                border_radius=8
            ),
            ft.Row([
                ft.ElevatedButton("⏪ Quay lại", on_click=on_back_click),
                ft.ElevatedButton("Tiếp theo" if self.current_step < 5 else "💾 Lưu", on_click=on_next_click if self.current_step < 5 else on_save_click),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        ])

    def build_step_1(self):
        def on_name_change(e):
            self.new_camera_data["name"] = e.control.value

        def on_location_change(e):
            self.new_camera_data["location"] = e.control.value

        return ft.Column([
            ft.Text("Bước 1: Nhập thông tin cơ bản"),
            ft.TextField(label="Tên thiết bị", on_change=on_name_change, value=self.new_camera_data["name"]),
            ft.TextField(label="Vị trí lắp đặt (tuỳ chọn)", on_change=on_location_change, value=self.new_camera_data["location"]),
        ])

    def build_step_2(self):
        def on_source_change(e):
            self.new_camera_data["source_type"] = e.control.value

        return ft.Column([
            ft.Text("Bước 2: Chọn nguồn video"),
            ft.RadioGroup(
                content=ft.Column([
                    ft.Radio(value="RTSP", label="RTSP"),
                    ft.Radio(value="File", label="File"),
                    ft.Radio(value="USB", label="USB"),
                ]),
                value=self.new_camera_data["source_type"],
                on_change=on_source_change
            ),
        ])

    def build_step_3(self):
        def on_url_change(e):
            self.new_camera_data["url"] = e.control.value

        def on_test_click(e):
            self.new_camera_data["test_status"] = len(self.new_camera_data["url"]) > 10  # Giả lập test
            test_status_text.value = f"Trạng thái: {'✅ Thành công' if self.new_camera_data['test_status'] else '❌ Thất bại'}"
            self.page.update()

        test_status_text = ft.Text(
            f"Trạng thái: {'✅ Thành công' if self.new_camera_data['test_status'] else '❌ Thất bại' if self.new_camera_data['test_status'] is False else 'Chưa kiểm tra'}"
        )

        return ft.Column([
            ft.Text("Bước 3: Nhập đường dẫn và kiểm tra kết nối"),
            ft.TextField(label="URL/Chọn file", on_change=on_url_change, value=self.new_camera_data["url"]),
            ft.ElevatedButton("🧪 Test Kết Nối", on_click=on_test_click),
            test_status_text,
        ])

    def build_step_4(self):
        return ft.Column([
            ft.Text("Bước 4: Xem trước luồng video"),
            ft.Container(
                content=ft.Text("🖥️ Preview khung nhỏ tại đây", italic=True),
                width=320,
                height=240,
                bgcolor=ft.colors.GREY_200,
                alignment=ft.alignment.center
            ),
        ])

    def build_step_5(self):
        return ft.Column([
            ft.Text("Bước 5: Xác nhận thông tin"),
            ft.Text(f"Tên thiết bị: {self.new_camera_data['name']}"),
            ft.Text(f"Vị trí: {self.new_camera_data['location'] or 'Không có'}"),
            ft.Text(f"Nguồn: {self.new_camera_data['source_type']}"),
            ft.Text(f"URL/File: {self.new_camera_data['url']}"),
            ft.Text(f"Trạng thái kết nối: {'Thành công' if self.new_camera_data['test_status'] else 'Thất bại'}"),
        ])

if __name__ == "__main__":
    app = CameraManagementApp()
    ft.app(target=app.main)
