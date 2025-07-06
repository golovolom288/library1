# Библиотека

Библиотека для удобного чтения книг в интернете, [ссылка на GitHub Pages](https://golovolom288.github.io/library1/pages/index1.html)

![Скриншот](https://github.com/golovolom288/library1/blob/main/screenshot.PNG)

## Запуск оффлайн

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub.

Установите зависимости:

```sh
pip install -r requirements.txt
```

Напишите в консоли данную команду, если не хотите каждый раз указывать путь до файла с книгами, то создайте файл .env в корне проекта и напишите в нём DEFAULT_DATA_FILEPATH="Ваш путь до файла"

```sh
python render_website.py "Ваш путь до файла с книгами"
```

Зайдите на сайт по [ссылке](http://127.0.0.1:5500)

## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).
