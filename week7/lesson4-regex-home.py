import re

# Напишите скрипт, который извлекает все хештеги (например, #python) из данного текста.
# Вы можете использовать регулярные выражения, чтобы найти все вхождения хештегов.
# Откройте текстовый файл для чтения.Прочитайте содержимое файла и сохраните его
# в строковой переменной.Напишите регулярное выражение, которое ищет и извлекает электронные
# адреса из текста.Используйте модуль re для выполнения поиска с помощью регулярного выражения.
# Сохраните найденные адреса в отдельный файл или выведите их на экран.

text = "Пример #pythonddтекста с хештегом #python и другими #хештегами, and #pyTHon"
x_reg = re.compile(r'#Python', re.IGNORECASE)
x_list = x_reg.finditer(text)
for i in x_list:
    print(i.group())

# Открыть текстовый файл для чтения
with open('file_testing.txt', 'r', encoding='utf-8') as file:
    text_1 = file.read()

# Найти все электронные адреса в тексте с помощью регулярного выражения
regular_expression = re.compile(r'\b[\w.-]+@[\w.-]+\.\w+\b')
addresses = regular_expression.findall(text_1)

# Вывести найденные адреса на экран
for address in addresses:
    print(address)

# Сохранить найденные адреса в новый файл
with open('found_addresses.txt', 'w', encoding='utf-8') as output_file:
    output_file.write("Найденные электронные адреса:\n")
    for address in addresses:
        output_file.write(address + '\n')

print("Адреса сохранены в файле 'found_addresses.txt'.")