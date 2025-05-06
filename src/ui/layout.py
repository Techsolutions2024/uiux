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

    # Module buttons data: title and color
    modules = [
        {"title": "Quản lý Thiết bị", "color": ft.colors.BLUE_400},
        {"title": "Phân tích & Sự kiện AI", "color": ft.colors.GREEN_400},
        {"title": "Quản lý Người dùng", "color": ft.colors.ORANGE_400},
        {"title": "Giám sát Trực tiếp", "color": ft.colors.PURPLE_400},
        {"title": "Lưu trữ & Phát lại", "color": ft.colors.RED_400},
        {"title": "Báo cáo & Phân tích", "color": ft.colors.TEAL_400},
        {"title": "Cảnh báo & Thông báo", "color": ft.colors.AMBER_400},
        {"title": "Bảo mật & Cài đặt", "color": ft.colors.BROWN_400},
        {"title": "Tích hợp & Tùy chỉnh", "color": ft.colors.CYAN_400},
    ]

    def on_button_click(e):
        page.snack_bar = ft.SnackBar(
            ft.Text(f"Bạn đã bấm nút: {e.control.data}"),
            open=True,
            duration=2000,
        )
        page.update()
        print(f"Button clicked: {e.control.data}")

    # Create buttons for modules with pixel positioning using margin
    buttons = []
    for i, module in enumerate(modules):
        btn = ft.ElevatedButton(
            text=module["title"],
            bgcolor=module["color"],
            color=ft.colors.WHITE,
            width=280,
            height=100,
            data=module["title"],
            on_click=on_button_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
                padding=10,
            ),
        )
        container = ft.Container(
            content=btn,
            margin=ft.margin.only(
                left=20 if i % 3 != 0 else 0,
                top=20 if i >= 3 else 0,
            ),
        )
        buttons.append(container)

    # Arrange buttons in 3 columns and 3 rows using Row and Column with pixel margin
    grid = ft.Column(
        [
            ft.Row(buttons[0:3], alignment=ft.MainAxisAlignment.START),
            ft.Row(buttons[3:6], alignment=ft.MainAxisAlignment.START),
            ft.Row(buttons[6:9], alignment=ft.MainAxisAlignment.START),
        ],
        spacing=0,
        alignment=ft.MainAxisAlignment.START,
    )

    # Main layout container with padding
    main_container = ft.Container(
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

    return main_container

def main(page: ft.Page):
    page.title = "Hệ thống Quản trị Camera"
    page.window_width = 1100
    page.window_height = 850
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    layout = create_main_layout(page)
    page.add(layout)

if __name__ == "__main__":
    ft.app(target=main)
