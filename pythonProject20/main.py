import flet as ft


def main(page: ft.Page):
    page.title = "Счетчик в окне"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    count = 0
    saved_count = 0

    count_display = ft.Text(str(count), size=30)
    message_display = ft.Text("")
    filename_input = ft.TextField(label="Введите имя файла (с расширением .txt)", width=300)

    def on_click_increment(e):
        nonlocal count
        count += 1
        count_display.value = str(count)
        message_display.value = ""
        page.update()

    def on_click_save(e):
        nonlocal saved_count, count
        saved_count = count
        message_display.value = f"Сохранено: {saved_count}"
        page.update()

        # Get the filename from the input field
        filename = filename_input.value if filename_input.value.endswith('.txt') else filename_input.value + '.txt'

        # Save the count to the specified text file
        with open(filename, "w") as file:
            file.write(str(saved_count))

    def on_click_reset(e):
        nonlocal count
        count = 0
        count_display.value = str(count)
        message_display.value = "Всё сброшено"
        page.update()

    increment_button = ft.ElevatedButton("Увеличить", on_click=on_click_increment)
    save_button = ft.ElevatedButton("Сохранить в файл", on_click=on_click_save)
    reset_button = ft.ElevatedButton("Сбросить", on_click=on_click_reset)

    page.add(
        ft.Column(
            [
                ft.Text("Текущий счет:"),
                count_display,
                filename_input,
                ft.Row(
                    [
                        increment_button,
                        save_button,
                        reset_button,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                message_display,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


ft.app(target=main)

