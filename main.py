# pythonProject5

# Берем текст из одного текстового файла, чистим текст от мусора, сохраняем в другой

# Название файла с текстом, если файл находится не в проекте, то писать полный путь:
# "C:/Users/Александр/OneDrive/Рабочий стол/python/FreelanceTask2/freelanceTask3/firstText.txt" (использ.:'/'!)
open_txt = "firstText.txt"

# Сюда записываем слова, строки с которыми необходимо убрать
stop_list = ['АНЕКДОТЫ', '2022', "2021", '2020', '2019', 'января', "анекдоты", "­", "97,2"]


# взять значения из текстового файла firstText.txt
def open_text1(text):
    """
    Открываем текстовый файл.
    :return: и сохраняет в список
    """
    file1 = open(text, encoding='utf-8')  # если файл находится не в проекте, то писать полный путь:
    # "C:/Users/Александр/OneDrive/Рабочий стол/python/FreelanceTask2/freelanceTask3/firstText.txt" (использ.:'/'!)
    file1_read = list(file1.read().split(sep='\n\n\n'))  # сохраняет данные из файла в список в str формате
    file1.close()  # закрывает файл
    return file1_read


# чистим текст строки и формируем анекдот
def clean_text(text):
    """
    Удаляем ненужное слово из анекдота.
    :param text: вводим текст
    :return: чистый текст
    """
    cl_text = str(text)
    # Добавляем пробелы
    cl_text = cl_text.replace(',', ', ')
    while ',  ' in cl_text:
        cl_text = cl_text.replace(',  ', ', ')
    cl_text = cl_text.replace('.', '. ')
    while '.  ' in cl_text:
        cl_text = cl_text.replace('.  ', '. ')
    cl_text = cl_text.replace('!', '! ')
    while '!  ' in cl_text:
        cl_text = cl_text.replace('!  ', '! ')
    cl_text = cl_text.replace('?', '? ')
    while '?  ' in cl_text:
        cl_text = cl_text.replace('?  ', '? ')
    cl_text = cl_text.replace(':', ': ')
    while ':  ' in cl_text:
        cl_text = cl_text.replace(':  ', ': ')
    cl_text = cl_text.replace('. . .', '... ')
    while '...  ' in cl_text:
        cl_text = cl_text.replace('...  ', '... ')
    # добавляем переносы
    while ":-" in cl_text:
        cl_text = cl_text.replace(":-", ":\n-")
    while ": -" in cl_text:
        cl_text = cl_text.replace(": -", ":\n-")
    while ".-" in cl_text:
        cl_text = cl_text.replace(".-", ".\n-")
    while ". -" in cl_text:
        cl_text = cl_text.replace(". -", ".\n-")
    while "?-" in cl_text:
        cl_text = cl_text.replace("?-", "?\n-")
    while "? -" in cl_text:
        cl_text = cl_text.replace("? -", ".\n-")
    while "!-" in cl_text:
        cl_text = cl_text.replace("!-", "!\n-")
    while "! -" in cl_text:
        cl_text = cl_text.replace("! -", "!\n-")
    while ":—" in cl_text:
        cl_text = cl_text.replace(":—", ":\n—")
    while ": —" in cl_text:
        cl_text = cl_text.replace(": —", ":\n—")
    while ".—" in cl_text:
        cl_text = cl_text.replace(".—", ".\n—")
    while ". —" in cl_text:
        cl_text = cl_text.replace(". —", ".\n—")
    while "?—" in cl_text:
        cl_text = cl_text.replace("?—", "?\n—")
    while "? —" in cl_text:
        cl_text = cl_text.replace("? —", ".\n—")
    while "!—" in cl_text:
        cl_text = cl_text.replace("!—", "!\n—")
    while "! —" in cl_text:
        cl_text = cl_text.replace("! —", "!\n—")
    # Удаляем ненужные слова
    if "Анекдоты:" in cl_text:
        # Удаляем ненужное слово из анекдота
        cl_text = cl_text[cl_text.find(':') + 1:]
    return cl_text


def delete_chort_text(text1):
    """
    Из текста 1 удаляет короткие и неполные рецепты
    :param text1: Список с рецептами
    :return: Список с рецептами
    """
    if "РЕЦЕПТ:" not in text1:
        text2 = None
    elif len(text1[:text1.index("РЕЦЕПТ:")]) < 50:
        text2 = None
    elif len(text1[text1.index("РЕЦЕПТ:"):]) < 100:
        text2 = None
    elif len(text1) < 250:
        text2 = None
    else:
        text2 = text1
    return text2


def search_women_verb(recipefunc, word_dict={}):
    """
    Ищем в рецепте глаголы женского рода (сделаЛА), составояем словарь {сделаЛА:сделаЛ}
    :param recipefunc: входной рецепт
    :param word_dict: словарь входной
    :return: выходной словарь
    """
    split_recipe = list(recipefunc.split())  # разделяем рецепт на слова
    for word in split_recipe:
        if '\n' in word:
            while '\n' in word:
                word = word.replace('\n', '')  # убираем переносы
        if len(word) > 2:  # если слово не короткое
            if word.lower()[-2:] == 'лa':  # 'a' - английская
                word_dict[word] = word[:-1]  # добавляем в словарь "делаЛА:делаЛ"
    return word_dict


def change_english_to_russian_letters(text):
    """
    Меняем английские заглавные буквы на русские
    :param text: изначальный тект (строка)
    :return: измененный тект
    """
    d_chars = {'A': 'А', 'B': 'В', 'E': 'Е', 'K': 'К', 'M': 'М', 'H': 'Н', 'O': 'О',
               'P': 'Р', 'C': 'С', 'T': 'Т', 'X': 'Х'}
    for char in d_chars:
        if char in text:
            while char in text:
                text = text.replace(char, d_chars[char])
    return text


fun_list = open_text1(open_txt)
# print(fun_list)
file2 = open("secondText.txt", 'w', encoding='utf-8')  # создается файл, 'w' - запись файла

# этот блок чистит текст
# Очищеная страница записывается в список 'jokes' и в текстовый файл 'secondText.txt'
jokes = []
# for joke in fun_list:
#    fl_stop = False
#   for stop in stop_list:
#       fl_stop = False
#       if stop in joke:
#           fl_stop = True
#       if fl_stop is True:
#           break
#   if fl_stop is False and joke != '':  # joke != '' - убираем пустые строки
#       jokes.append(clean_text(joke))
#       file2.write(clean_text(joke) + '\n\n')

# этот блок удаляет короткие рецепты
for recipe in fun_list:
    if delete_chort_text(recipe) != None:
        jokes.append(recipe)
        file2.write(recipe + '\n\n\n')
print("Количество рецептов ",len(jokes))
# этот блок переводит глаголы женского рода в мужской
# словарь с заменами слов
# word_d = {}
# for recipe in fun_list:
#    word_d = search_women_verb(recipe, word_dict=word_d)
# file2.write(f"{word_d}" + '\n\n\n')

# этот блок меняет английские заглавные буквы на русские
# for recipe in fun_list:
#    recipe = change_english_to_russian_letters(recipe)
#    file2.write(recipe + '\n\n\n')

file2.close()  # закрывает файл
# print(word_d)
# print("Количество пар слов в словаре", len(word_d))
