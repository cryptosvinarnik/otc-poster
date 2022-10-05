import asyncio
import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from telethon import TelegramClient


print('Created by @cryptosvinarnik')

api_id, api_hash = '', ''  # сюда данные с сайта
groups = []  # сюда айди ОТС (пример: groups = [-1004413432, 'https://t.me/cryptosvinarnik'])

client = TelegramClient('otc', api_id, api_hash)
scheduler = BackgroundScheduler()
scheduler.start()
client.start()

loop = asyncio.get_event_loop()


def send_messages():
    with open('message.txt', encoding='utf-8') as f:
        message_text = f.read()

    for group in groups:
        try:
            loop.run_until_complete(client.send_message(group, message_text))
            time.sleep(.09)
        except Exception as e:
            print(e)


scheduler.add_job(
    send_messages,
    trigger=IntervalTrigger(
        hours=int(input('Delay between messages (in hours):'))
    )
)
send_messages()
input('Press Enter to exit!')
