# Ваше завдання написати функцію, яка прочитає заданий файл, очистить текст
# від html-тегів і запише цей текст в інший файл. html-тег завжди починається
# з "<" і закінчується на ">" тобто. потрібно видалити ці символи та все, що
# між ними. Функція отримує на вхід два параметри – ім'я файлу, який потрібно
# очистити, та ім'я файлу, куди потрібно записати очищений текст. Ім'я файлу,
# куди потрібно писати, можна задати за замовчуванням.
# Приклади файлів у вкладенні – файл який потрібно очистити (draft.html) та
# приклад файлу, який може вийти на виході з очищеним текстом (cleaned.txt).
# Файл draft.html необхідно скачати і покласти поряд з файлом, де буде
# вирішення цієї домашки.
#
# Додаткове завдання для тих, хто захоче ускладнити рішення - спробуйте
# прибрати рядки, в яких немає інформації.


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, encoding='utf-8') as file:
        input_data = file.readlines()

    output_data = []
    for line in input_data:
        line = line.strip('\n').strip()
        if line:
            new_line = ''
            tag = False
            for symbol in line:
                if symbol == '<':
                    tag = True
                    continue
                if symbol == '>':
                    tag = False
                    continue
                if tag is False:
                    new_line += symbol

            if new_line:
                output_data.append(new_line)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(output_data))


delete_html_tags('draft.html')
