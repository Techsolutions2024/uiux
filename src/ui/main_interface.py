import flet as ft

class CameraRow(ft.Row):
    def __init__(self, name, connection_type, status, location, on_edit, on_delete, on_configure):
        super().__init__()
        self.name = name
        self.connection_type = connection_type
        self.status = status
        self.location = location
        self.on_edit = on_edit
        self.on_delete = on_delete
        self.on_configure = on_configure
        self.controls = [
            ft.Text(self.name),
            ft.Text(self.connection_type),
            ft.Text(self.status),
            ft.Text(self.location),
            ft.IconButton(ft.icons.EDIT, on_click=self.on_edit),
            ft.IconButton(ft.icons.DELETE, on_click=self.on_delete),
            ft.IconButton(ft.icons.SETTINGS, on_click=self.on_configure),
        ]

class CameraApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.camera_rows = []
        self.new_camera_name = ft.TextField(hint_text="Tên camera mới")
        self.new_camera_location = ft.TextField(hint_text="Vị trí")
        self.new_camera_connection_type = ft.Dropdown(
            options=["RTSP", "USB", "File", "HTTP"], hint_text="Chọn loại kết nối"
        )
        self.new_camera_status = ft.Dropdown(
            options=["🟢 Online", "🔴 Offline", "🟡 Lỗi"], hint_text="Trạng thái"
        )
        self.add_camera_button = ft.FloatingActionButton(
            icon=ft.icons.ADD, on_click=self.add_camera
        )
        self.controls = [
            self.new_camera_name,
            self.new_camera_location,
            self.new_camera_connection_type,
            self.new_camera_status,
            self.add_camera_button,
            ft.Column(controls=self.camera_rows),
        ]

    def add_camera(self, e):
        name = self.new_camera_name.value
        location = self.new_camera_location.value
        connection_type = self.new_camera_connection_type.value
        status = self.new_camera_status.value
        row = CameraRow(
            name,
            connection_type,
            status,
            location,
            on_edit=self.edit_camera,
            on_delete=self.delete_camera,
            on_configure=self.configure_camera,
        )
        self.camera_rows.append(row)
        self.new_camera_name.value = ""
        self.new_camera_location.value = ""
        self.new_camera_connection_type.value = ""
        self.new_camera_status.value = ""
        self.update()

    def edit_camera(self, e):
        pass  # Implement edit functionality

    def delete_camera(self, e):
        self.camera_rows.remove(e.control.parent)
        self.update()

    def configure_camera(self, e):
        pass  # Implement configure functionality

def main(page: ft.Page):
    page.add(CameraApp())

ft.app(target=main)
