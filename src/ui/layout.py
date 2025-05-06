import flet as ft

def create_main_layout(page: ft.Page):
    # Header
    header = ft.Column(
        [
            ft.Text(
                "Hệ thống Quản trị Camera",
                size=30,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_900,
            ),
            ft.Text(
                "Phần mềm quản lý camera, AI, lưu trữ, bảo mật, báo cáo, rủi ro",
                size=16,
                color=ft.colors.BLUE_700,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=5,
        expand=False,
    )

    # Module cards data: title and description
    modules = [
        {
            "title": "Quản lý Thiết bị",
            "desc": "Camera, Cảm biến IoT, trạng thái thiết bị",
        },
        {
            "title": "Phân tích & Sự kiện AI",
            "desc": "Nhận diện, cảnh báo, phân tích dự đoán",
        },
        {
            "title": "Quản lý Người dùng",
            "desc": "Phân quyền, nhật ký, xác thực hai yếu tố (2FA)",
        },
        {
            "title": "Giám sát Trực tiếp",
            "desc": "Live View, PTZ, trạng thái camera",
        },
        {
            "title": "Lưu trữ & Phát lại",
            "desc": "Video, metadata, tìm kiếm, xuất video",
        },
        {
            "title": "Báo cáo & Phân tích",
            "desc": "Dashboard, dự đoán, báo cáo tùy chỉnh",
        },
        {
            "title": "Cảnh báo & Thông báo",
            "desc": "Email, SMS, app, lịch sử thông báo",
        },
        {
            "title": "Bảo mật & Cài đặt",
            "desc": "Mã hóa, backup, audit, kiểm tra bảo mật",
        },
        {
            "title": "Tích hợp & Tùy chỉnh",
            "desc": "ONVIF, RESTful API, SDK, giao thức IoT",
        },
    ]

    def on_module_click(e):
        dlg = ft.AlertDialog(
            title=ft.Text("Chức năng đang phát triển"),
            content=ft.Text(f"Bạn đã chọn module: {e.control.data}"),
            actions=[ft.TextButton("Đóng", on_click=lambda e: dlg.close())],
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    # Create cards for modules
    cards = []
    for module in modules:
        card = ft.Container(
            content=ft.Column(
                [
                    ft.Text(module["title"], size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(module["desc"], size=14, color=ft.colors.BLUE_GREY),
                ],
                tight=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=20,
            alignment=ft.alignment.center,
            width=250,
            height=120,
            bgcolor=ft.colors.WHITE,
            border_radius=10,
            border=ft.border.all(1, ft.colors.BLUE_200),
            shadow=ft.BoxShadow(
                color=ft.colors.BLUE_200,
                blur_radius=5,
                offset=ft.Offset(2, 2),
            ),
            data=module["title"],
            on_click=on_module_click,
        )
        cards.append(card)

    # Arrange cards in 3 columns and 3 rows
    grid = ft.Column(
        [
            ft.Row(cards[0:3], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
            ft.Row(cards[3:6], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
            ft.Row(cards[6:9], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Main layout column
    main_column = ft.Container(
        content=ft.Column(
            [
                header,
                ft.Divider(height=2, thickness=2, color=ft.colors.BLUE_900),
                grid,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
            expand=True,
            scroll=ft.ScrollMode.AUTO,
        ),
        padding=20,
    )

    return main_column

def main(page: ft.Page):
    page.title = "Hệ thống Quản trị Camera"
    page.window_width = 1000
    page.window_height = 800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    layout = create_main_layout(page)
    page.add(layout)

if __name__ == "__main__":
    ft.app(target=main)
