import asyncio
import os
import logging
from telethon import TelegramClient
from telethon.sessions import StringSession
# Настройка логирования
logging.basicConfig(filename = "C:\\Users\\Windows\\Documents\\tg_spam\\log.txt", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s' , encoding='utf-8' )

# Введи свои данные, которые ты получил на сайте my.telegram.org
api_id = '24567310'
api_hash = 'c28c7db6566293ceb5d02a3f964e65f3'
phone_number = '+79789493049'

session_string = os.getenv('TELEGRAM_SESSION')

if session_string:
    client = TelegramClient(StringSession(session_string), api_id, api_hash)
else:
    client = TelegramClient(StringSession(), api_id, api_hash)
# Сообщение, которое будет отправляться
message = """📢 Ищем сотрудников! 

📆 Возраст от 16 лет и старше! 

💵 Пассивный заработок , оплата на еженедельной так и на ежедневной основе ! 

✨ Основные требования:
1) 💻 Наличие avito обязательно! 💻
2) 💳 Наличие банковской карты для получения оплаты на ежедневной/еженедельной основе ! 💸

💻 Ваше задание  : 
👨‍💻Нужно оставлять отзывы и продвиpython tg_send.py
гать товары определенных компаний на площадке avito , каждый отзыв оплачивается в 250 рублей + 1200 рублей за рекламу в соцсетях !👨‍💻
⚡️Также есть возможность сдать в аренду ваш аккаунт avito , от 10000 рублей   ⚡️
💸Цена зависит от количества отзывов ,  продаж и даты регистрации.💸


 💌 по всем вопросам-
📌 Telegram 
✉️✉️За более детальное информацией пишите в личные сообщения !!✉️✉️"""

# Создаем клиента
async def send_message_to_groups():
    # Подключаемся к Telegram
    if not session_string:
        await client.start(phone=phone_number)
        new_session_string = client.session.save()
        logging.info("Сохраните строку сессии и добавьте её в переменные окружения: ")
        logging.info(new_session_string)

    # Получаем список диалогов (групп и чатов)
    async for dialog in client.iter_dialogs():
        # Проверяем, что это группа (supergroup или обычная group)
        if dialog.is_group:
            logging.info(f"Отправка сообщения в группу: {dialog.name}")
            try:
                # Отправляем сообщение в группу
                await client.send_message(dialog.id, message)
                # Пауза 20 секунд перед отправкой в следующую группу
                await asyncio.sleep(20)
            except Exception as e:
                logging.error(f"Не удалось отправить сообщение в {dialog.name}: {str(e)}")

    # Закрываем клиент после отправки сообщений во все группы
    await client.disconnect()
    logging.info("Все сообщения отправлены.")

# Запуск основной функции
with client:
    client.loop.run_until_complete(send_message_to_groups())