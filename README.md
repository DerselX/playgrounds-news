# 📕 Предисловие

Парсер актуальных новостей на платформе **playgrounds** посредством Telegram-бота. 

## 📷 Скриншот

<img width="306" height="283" alt="image" src="https://github.com/user-attachments/assets/535bf5b3-e4cb-46fe-8ca0-b2539f79485e" />

## 📁Технологии
- Парсинг: **bs4**
- http-клиент: **requests**
- telegram-бот: **aiogram**

## 📌 Как использовать?
1) Установите необходимые модули для работы скрипта:
```cmd
pip install -r requirements txt
```

2) Далее в файле `.env` укажите необходимые параметры:
```cmd
BOT_TOKEN=токен бота
CHANNEL_ID=айди канала
```
3) Запуск:
```cmd
python bot.py
```
