# Отправка фотографий космоса в Telegram-канал
Три файла, которые скачивают фотографии связанные с космосом

telegram_bot_img.py - Публикует одну фотографию каждые 4 часа (Время 4 часа - по умолчанию. Можно поменять через переменную окружения)
fetch_spacex_images.py - Скачивает изображения последнего запуска корабля SpaceX, если не указан номер конкретного запуска  
fetch_apod_images.py - Скачивает лучшие фотографии от NASA  
fetch_epic_images.py - Скачивает изображения земли  
get_type_img.py - Выдает тип файла по URL-ссылке  

### Как установить и настроить

Python уже должен быть установлен
Затем используйте `pip` для установки зависимостей

```pip install -r requirements.txt```

Не забудьте создать файл для переменных окружения `.env` и прописать туда ваш токен от сервиса https://api.nasa.gov/  
`TELEGRAM_TOKEN` - Токен вашего бота в Telegram  

Пример содержимого файла `.env`

```NASA_TOKEN='123456789123456789'```  
```TELEGRAM_TOKEN = '123456789123456789'```  
```TIME_SLEEP = 60```  
```COUNT_APOD = 30```  
```CHAT_ID_TELEGRAM = '@name_channel'```  

TIME_SLEEP - пауза между отправками фотографии указывается в секундах. По умолчанию 4 часа - 14400 секунд.  
COUNT_APOD - количество фотографии, которые нужно скачать. Переменная для скрипта `fetch_apod_images.py`  
CHAT_ID_TELEGRAM - ID Telegram канала, можно указать в числовом виде или через символ `@`

Рекомендуется использоваться Виртуальное окружение (venv)

### Как запустить

Запуск из терминала Linux с указанием папки с изображениями (обязательное поле)

```python3 send_telegram_img.py images```

### Цель проекта

Учебный проект по отправке изображений космоса в Telegram от онлайн-курса Devman (dvmn.org)