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

```
pip install -r requirements.txt
```  

Не забудьте создать файл для переменных окружения `.env` и прописать туда ваш токен от сервиса https://api.nasa.gov/  

`TELEGRAM_TOKEN` - Токен вашего бота в Telegram  

Пример содержимого файла `.env`

```
NASA_TOKEN='123456789123456789' 
TELEGRAM_TOKEN='123456789123456789'
SLEEP_TIME=60
TELEGRAM_CHAT_ID='@name_channel'
```

SLEEP_TIME - пауза между отправками фотографии указывается в секундах. По умолчанию 4 часа - 14400 секунд.  
TELEGRAM_CHAT_ID - ID Telegram канала, можно указать в числовом виде или через символ `@`  

Рекомендуется использоваться Виртуальное окружение (venv)

### Как запустить

Запуск из терминала Linux с указанием папки с изображениями (необязательное поле, по умолчанию название папки images)

```
python3 send_telegram_img.py images
```  

Запуск отдельных скриптов по скачиванию изображений  

```
python3 fetch_apod_images.py number
```  

Где number - количество фотографии, которые нужно скачать. Необязательное поле, по умолчанию значение 15.  

```
python3 fetch_spacex_images.py launch_id
```  

`launch_id` - это ID запуска корабля SpaceX. Если не будет указано значение, то возьметься последний запуск.  

```
python3 fetch_epic_images.py
```  


### Цель проекта

Учебный проект по отправке изображений космоса в Telegram от онлайн-курса Devman (dvmn.org)