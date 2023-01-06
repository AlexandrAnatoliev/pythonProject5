# pythonProject5

[Ru] Очиститель текста

## Описание:

Берем текст из одного текстового файла, чистим текст от мусора, сохраняем в другой

## Требования

* создать файл firstText.txt в который скопировать текст, кторый необходимо очистить

## Примеры использования

#### Название файла с текстом

#### Если файл находится не в проекте, то писать полный путь: "C:/Users/Александр/OneDrive/Рабочий стол/python/FreelanceTask2/freelanceTask3/firstText.txt" (использ.:'/'!)

```python
open_txt = "firstText.txt"
```

#### Сюда записываем слова, строки с которыми необходимо убрать

```python
stop_list = ['АНЕКДОТЫ', '2022', "2021", '2020', '2019', 'января', "анекдоты", "­"]
```

#### Чистим текст строки и формируем анекдот

#### В данном случае удаляем "Анекдоты:" из начала строки

```python
def clean_text(text):
    """
    Удаляем ненужное слово из анекдота.
    :param text: вводим текст
    :return: чистый текст
    """
    cl_text = str(text)
    if "Анекдоты:" in cl_text:
        # Удаляем ненужное слово из анекдота
        cl_text = cl_text[cl_text.find(':') + 1:]
    return cl_text
```
#### Из текста 1 удаляет короткие и неполные рецепты
```python
def delete_chort_text(text1):
    if "PEЦEПT:" not in text1:
        text2 = None
    elif len(text1[:text1.index("PEЦEПT:")]) < 5:
        text2 = None
    elif len(text1[text1.index("PEЦEПT:"):]) < 5:
        text2 = None
    else:
        text2 = text1
    return text2
```
#### Очищеная страница записывается в список 'jokes' и в текстовый файл 'secondText.txt'
#### Записываем строки не содержащие слова из стоп-листа и не пустые "joke != ''"

```python
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
        file2.write(clean_text(joke) + '\n')
```

#### Не забываем открывать файл перед использованием

```python
file2 = open("secondText.txt", 'w', encoding='utf-8')  # создается файл, 'w' - запись файла
```

#### И закрывать его - после

```python
file2.close()  # закрывает файл
```