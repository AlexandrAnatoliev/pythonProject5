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
    file1_read = list(file1.read().split(sep='\n\n'))  # сохраняет данные из файла в список в str формате
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
    while ":-" in cl_text:
        cl_text= cl_text.replace(":-",":\n-")
    while ": -" in cl_text:
        cl_text= cl_text.replace(": -",":\n-")
    while ".-" in cl_text:
        cl_text= cl_text.replace(".-",".\n-")
    while ". -" in cl_text:
        cl_text= cl_text.replace(". -",".\n-")
    if "Анекдоты:" in cl_text:
        # Удаляем ненужное слово из анекдота
        cl_text = cl_text[cl_text.find(':') + 1:]
    return cl_text


fun_list = open_text1(open_txt)
print(fun_list)

file2 = open("secondText.txt", 'w', encoding='utf-8')  # создается файл, 'w' - запись файла

# Очищеная страница записывается в список 'jokes' и в текстовый файл 'secondText.txt'
jokes = []
for joke in fun_list:
    fl_stop = False
    for stop in stop_list:
        fl_stop = False
        if stop in joke:
            fl_stop = True
        if fl_stop is True:
            break
    if fl_stop is False and joke != '':  # joke != '' - убираем пустые строки
        jokes.append(clean_text(joke))
        file2.write(clean_text(joke) + '\n\n')

file2.close()  # закрывает файл
print(jokes)
